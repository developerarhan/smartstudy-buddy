import os
import json
import re
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def extract_json(text):
    """
    Extract JSON array from AI output safely
    """
    match = re.search(r"\[.*\]", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON array found in AI response")
    return json.loads(match.group())


def generate_study_plan(subject, hours_per_day, days):
    try:
        prompt = f"""
You are an AI that ONLY returns valid JSON.
DO NOT explain anything.
DO NOT use markdown.
DO NOT add extra text.

Return ONLY this JSON array format:

[
  {{
    "day": 1,
    "topic": "Topic name",
    "hours": {hours_per_day}
  }}
]

Generate a {days}-day study plan for {subject}.
Each day has {hours_per_day} hours.
Difficulty increases gradually.
Include revision and practice.
"""

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You generate strict JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4
        )

        raw_text = response.choices[0].message.content.strip()

        return extract_json(raw_text)

    except Exception as e:
        print("❌ Groq failed, using fallback:", e)
        return fallback(subject, hours_per_day, days)


def fallback(subject, hours_per_day, days):
    return [
        {
            "day": i + 1,
            "topic": f"{subject} - Core Concept {i + 1}",
            "hours": hours_per_day
        }
        for i in range(days)
    ]