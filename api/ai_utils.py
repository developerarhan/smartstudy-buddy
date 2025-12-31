def generate_study_plan(subject, hours_per_day, days, use_ai=False):
    if use_ai:
        return ai_generated_plan(subject, hours_per_day, days)

    return [
        {
            "day": day,
            "topic": f"{subject} - Topic {day}",
            "hours": hours_per_day
        }
        for day in range(1, days + 1)
    ]
