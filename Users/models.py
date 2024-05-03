from django.db import models
from UserProfile.models import User
from Coaches.models import Coach

class Athlet(models.Model):
    athlet_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    Goal = models.CharField(max_length=120)
    Maladies = models.CharField(max_length=120)
    SkillLevel = models.CharField(max_length=120)
    Bmiscore = models.FloatField()
    assigned_coach = models.ForeignKey(Coach, on_delete=models.SET_NULL, null=True, blank=True, related_name='athlets')

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None)
    skills = models.CharField(max_length=120)
    Permissions = models.CharField(max_length=120)