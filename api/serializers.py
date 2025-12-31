from rest_framework import serializers

class StudyPlanSerializer(serializers.Serializer):
    subject = serializers.CharField()
    hours_per_day = serializers.IntegerField()
    days = serializers.IntegerField()