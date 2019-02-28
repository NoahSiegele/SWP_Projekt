from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Teacher, Student, Noten, Subject, Klasse


class IndexView(generic.ListView):
    template_name = 'noten/startseite.html'

