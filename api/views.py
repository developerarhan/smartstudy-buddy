from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import StudyPlanSerializer
from .ai_utils import generate_study_plan
from .models import StudyPlan

# Create your views here.

@api_view(['POST'])
def study_plan(request):
    serializer = StudyPlanSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(
            {"success": False, "errors": serializer.errors},
            status=400
        )

    data = serializer.validated_data

    plan = generate_study_plan(
        data["subject"],
        data["hours_per_day"],
        data["days"]
    )

    StudyPlan.objects.create(
        subject=data["subject"],
        hours_per_day=data["hours_per_day"],
        days=data["days"]
    )

    return Response({
        "success": True,
        "data": {
            "subject": data["subject"],
            "total_days": data["days"],
            "plan": plan
        }
    })

@api_view(['GET'])
def health(request):
    return Response({"status": "ok"})

@api_view(['GET'])
def study_plan_history(request):
    plans = StudyPlan.objects.all().order_by('-created_at')
    data = [
        {
            "subject": p.subject,
            "hours_per_day": p.hours_per_day,
            "days": p.days,
            "created_at": p.created_at
        }
        for p in plans
    ]
    return Response(data)
