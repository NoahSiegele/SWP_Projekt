from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Klasse, Student, Teacher, Subject, Noten

class IndexView(generic.ListView):
    template_name = 'noten_webseiten/startseite_lehrer.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Teacher.username