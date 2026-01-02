import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def extract_json(text):
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON array found")
    return json.loads(match.group())


# 🔹 NEW: Hour-wise block splitter
def split_hours_into_blocks(total_hours, base_topic):
    blocks = []

    if total_hours == 1:
        blocks.append({
            "duration": 1,
            "topic": f"Introduction to {base_topic}",
            "type": "theory"
        })

    elif total_hours == 2:
        blocks.extend([
            {"duration": 1, "topic": f"Core concepts of {base_topic}", "type": "theory"},
            {"duration": 1, "topic": f"Practice problems on {base_topic}", "type": "practice"},
        ])

    else:
        blocks.extend([
            {"duration": 1, "topic": f"Basics of {base_topic}", "type": "theory"},
            {"duration": 1, "topic": f"Advanced concepts of {base_topic}", "type": "theory"},
        ])

        for _ in range(total_hours - 2):
            blocks.append({
                "duration": 1,
                "topic": f"Hands-on + revision of {base_topic}",
                "type": "revision"
            })

    return blocks


# 🔹 UPDATED AI PLAN GENERATOR
def generate_study_plan(subject, hours_per_day, days):
    try:
        prompt = f"""
You are an AI that ONLY returns valid JSON.
No markdown. No explanation.

Return ONLY this JSON array:

[
  {{
    "day": 1,
    "title": "Topic name"
  }}
]

Generate {days} days for subject {subject}.
Each day should have ONE main topic.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You return strict JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        raw = response.choices[0].message.content.strip()
        ai_days = extract_json(raw)

        # 🧠 Convert AI topics → hour-wise blocks
        plan = []

        for day in ai_days:
            blocks = split_hours_into_blocks(hours_per_day, day["title"])

            plan.append({
                "day": day["day"],
                "title": day["title"],
                "total_hours": hours_per_day,
                "blocks": blocks
            })

        return plan

    except Exception as e:
        print("❌ Groq failed, using fallback:", e)
        return fallback(subject, hours_per_day, days)


# 🔹 FALLBACK (NO AI NEEDED)
def fallback(subject, hours_per_day, days):
    plan = []

    for i in range(days):
        title = f"{subject} - Core Concept {i + 1}"
        blocks = split_hours_into_blocks(hours_per_day, title)

        plan.append({
            "day": i + 1,
            "title": title,
            "total_hours": hours_per_day,
            "blocks": blocks
        })

    return plan