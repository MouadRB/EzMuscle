from django.db import models
from Users.models import Athlet

class Progress(models.Model):
    athlet = models.ForeignKey(Athlet, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.PositiveIntegerField()
    bmi = models.FloatField()
    fitness_level = models.CharField(max_length=120)
    notes = models.TextField(blank=True)
