# smartstudy-buddy

## Study Plan API

POST /api/study-plan/

Request:
{
  "subject": "Mathematics",
  "hours_per_day": 3,
  "days": 7
}

Response:
{
  "plan": [
    { "day": 1, "topic": "Mathematics - Topic 1", "hours": 3 }
  ]
}