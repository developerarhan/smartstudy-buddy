from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudyPlanSerializer
from .ai_utils import generate_study_plan
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def study_plan(request):
    serializer = StudyPlanSerializer(data=request.data)

    if not serializer.is_valid():
        return Response(
            {"error": "Invalid input", "details": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    data = serializer.validated_data
    plan = generate_study_plan(
        data['subject'],
        data['hours_per_day'],
        data['days']
    )

    return Response(
        {"plan": plan},
        status=status.HTTP_200_OK
    )