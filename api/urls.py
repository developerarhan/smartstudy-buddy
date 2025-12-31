from django.urls import path
from . import views

urlpatterns = [
    path('study-plan/', views.study_plan),
]
