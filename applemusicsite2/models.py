from django.db import models
from django.db.models.deletion import CASCADE
class register(models.Model):
    firstname=models.CharField(max_length=70)
    lastname=models.CharField(max_length=70)
    email=models.CharField(max_length=90,unique=True)
    phn=models.CharField(max_length=90,unique=True)
    plan=models.CharField(max_length=70)
    password=models.CharField(max_length=80)
# Create your models here.
