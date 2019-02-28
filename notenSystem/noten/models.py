from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Person(models.Model):
    username = models.CharField(default="", max_length=250)
    password = models.CharField(default="", max_length=50)
    email = models.CharField(default="", max_length=150)
    teacher = models.BooleanField(default=False)
    klasse = models.CharField(max_length=50, default="")

class Klasse(models.Model):
    class_name = models.CharField(default="", max_length=150)
    subjects = models.CharField(default="", max_length=150)





