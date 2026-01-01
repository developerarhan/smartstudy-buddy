from rest_framework import serializers

class StudyPlanSerializer(serializers.Serializer):
    subject = serializers.CharField(max_length=100)
    hours_per_day = serializers.IntegerField(min_value=1, max_value=12)
    days = serializers.IntegerField(min_value=1, max_value=60)