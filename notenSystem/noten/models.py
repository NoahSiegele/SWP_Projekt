from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(default="", max_length=250)
    password = models.CharField(default="", max_length=50)
    email = models.CharField(default="", max_length=150)
    klasse = models.CharField(max_length=50, default="")

class Klasse(models.Model):
    class_name = models.CharField(default="", max_length=150)

class Teacher(models.Model):
    username = models.CharField(default="", max_length=250)
    password = models.CharField(default="", max_length=50)
    email = models.CharField(default="", max_length=150)

class Subject(models.Model):
    subject_name = models.CharField(default="", max_length=150)

class Unterricht(models.Model):
    name = models.CharField(default="", max_length=150)
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
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





