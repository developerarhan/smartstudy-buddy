from django.urls import path
from .views import health, study_plan, study_plan_history

urlpatterns = [
    path('study-plan/', study_plan),
    path("health/", health),
    path('history/', study_plan_history),
]
