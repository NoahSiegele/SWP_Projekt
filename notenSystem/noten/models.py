from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Student(models.Model):
    username = models.CharField(default="", max_length=250)
    password = models.CharField(default="", max_length=50)
    email = models.CharField(default="", max_length=150)
    klasse = models.CharField(max_length=50, default="")

class Teacher(models.Model):
    username = models.CharField(default="", max_length=250)
    password = models.CharField(default="", max_length=50)
    email = models.CharField(default="", max_length=150)
    Klasse = models.ForeignKey(Klasse, on_delete=models.CASCADE)

class Klasse(models.Model):
    class_name = models.CharField(default="", max_length=150)
    subjects = models.CharField(default="", max_length=150)
    teacher = models.CharField(default="", max_length=150)


class Subject(models.Model):
    noten = models.IntegerField(default=0)
    Klasse = models.ForeignKey(Klasse, on_delete=models.CASCADE)
    teacher = models.CharField(default="", max_length=150)
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)


class Noten(models.Model):
    noten = models.IntegerField(default=0)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Klasse = models.ForeignKey(Klasse, on_delete=models.CASCADE)







