from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudyPlanSerializer
from .ai_utils import generate_study_plan

# Create your views here.

@api_view(['POST'])
def study_plan(request):
    serializer = StudyPlanSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        plan = generate_study_plan(
            data['subject'],
            data['hours_per_day'],
            data['days']
        )
        return Response({"plan": plan})
    return Response(serializer.errors, status=400)