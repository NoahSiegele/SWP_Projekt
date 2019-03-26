from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Klasse(models.Model):
    class_name = models.CharField(default="", max_length=150)

    def __str__(self):
        return self.class_name

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    klasse = models.ForeignKey(Klasse, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Students"

class Subject(models.Model):
    subject_name = models.CharField(default="", max_length=150)

    def __str__(self):
        return self.subject_name

class Unterricht(models.Model):
    Subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    Teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    Klasse = models.ForeignKey(Klasse, on_delete=models.CASCADE)

    def __str__(self):
        return self.Subject.subject_name

    class Meta:
        verbose_name_plural = "Unterrichte"

class Note(models.Model):
    note = models.IntegerField(default=0)
    type = models.CharField(default="", max_length=150)
    Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    Unterricht = models.ForeignKey(Unterricht, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Noten"

class Test(models.Model):
    Note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Teste"

class Prüfung(models.Model):
    Note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Prüfungstyp"





