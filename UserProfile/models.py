from django.db import models

class User(models.Model):
    fullname = models.CharField(max_length=120, null=True)
    date_of_birth = models.DateField(default='2000-01-01')
    gender = models.CharField(max_length=10, null=True)
    PhoneNumber = models.CharField(max_length=20, null=True)
    EmailAddress = models.EmailField(unique=True, null=True)
    Password = models.CharField(max_length=120, null=True)
