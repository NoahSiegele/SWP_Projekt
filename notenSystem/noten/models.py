from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Klasse(models.Model):
    class_name = models.CharField(default="", max_length=150)


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    klasse = models.ForeignKey(Klasse, on_delete=models.SET_NULL, null=True, blank=True)
    # username = models.CharField(default="", max_length=250)
    # password = models.CharField(default="", max_length=50)
    # klasse = models.CharField(max_length=50, default="")

class Subject(models.Model):
    subject_name = models.CharField(default="", max_length=150)

class Unterricht(models.Model):
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    Klasse = models.ForeignKey(Klasse, on_delete=models.CASCADE)

class Note(models.Model):
    note = models.IntegerField(default=0)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)

class Prüfung(models.Model):
    note = models.IntegerField(default=0)
    Note = models.ForeignKey(Note, on_delete=models.CASCADE)

class Test(models.Model):
    note = models.IntegerField(default=0)
    Note = models.ForeignKey(Note, on_delete=models.CASCADE)





