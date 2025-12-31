def generate_study_plan(subject, hours_per_day, days):
    plan = []
    for day in range(1, days+1):
        plan.append({
            "day": day,
            "topic": f"{subject} - Topic {day}",
            "hours": hours_per_day
        })
        return plan