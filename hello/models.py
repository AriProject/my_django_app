from django.db import models

# Create your models here.

#timer model to record time spent on questionnaire
class QuestionaireTime(models.Model):
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    time_spent = models.DurationField()

