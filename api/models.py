from django.db import models

# Create your models here.

class StudyPlan(models.Model):
    subject = models.CharField(max_length=100)
    hours_per_day = models.IntegerField()
    days = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} ({self.days} days)"