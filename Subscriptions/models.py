from django.db import models
from Users.models import Athlet


class CreditCard(models.Model):
    Cardnumber = models.PositiveIntegerField()
    HolderName = models.CharField(max_length=120)
    ExpirationDate = models.DateField()
    cvv = models.PositiveIntegerField()
    Card_Type = models.CharField(max_length=120)
    athlet = models.ForeignKey(Athlet, on_delete=models.CASCADE)

class Subscription(models.Model):
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10)
    Type = models.CharField(max_length=120)
    StartDate = models.DateField()
    EndDate = models.DateField()
    athlet = models.ForeignKey(Athlet, on_delete=models.CASCADE)