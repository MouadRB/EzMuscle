from django.db import models
from Subscriptions.models import Subscription

class Exercice(models.Model):
    NameExercice = models.CharField(max_length=120)
    Description = models.CharField(max_length=120)
    Url = models.URLField()
    difficulty_level = models.CharField(max_length=120, default="INTERMEDIATE")
    MostActiveMuscle = models.CharField(max_length=120)
    Equipments = models.CharField(max_length=120)

class Repitition(models.Model):
    sets = models.PositiveSmallIntegerField()
    rep = models.PositiveSmallIntegerField()
    duration = models.PositiveSmallIntegerField()
    weight = models.PositiveIntegerField(null=True)
    exercice = models.ForeignKey(Exercice, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE)