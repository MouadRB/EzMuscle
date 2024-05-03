from django.db import models
from UserProfile.models import User

class Coach(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    experience = models.PositiveSmallIntegerField()
    certifcat = models.CharField(max_length=120)
    skillLevel = models.CharField(max_length=120)
    isAvailable = models.BooleanField()
    TrainingGender = models.CharField(max_length=120)