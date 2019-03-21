from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Klasse, Student, Test, Subject, Prüfung, Note, Unterricht, User

class IndexView(generic.ListView):
    template_name = 'registration/login.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return "test"


@login_required
def index(request):
    usergroups = request.user.groups.all()
    names = []
    for g in usergroups:
        names.append(g.name)
        if 'Teacher' in names:
            return HttpResponseRedirect('/startseite_lehrer')
        elif 'Student' in names:
            return HttpResponseRedirect('/startseite_schueler')

class detailseite_lehrerView(LoginRequiredMixin, generic.ListView):
    model = Student
    template_name = 'noten/detailseite_lehrer.html'

    def get_queryset(self):
        return "test"

@login_required
def detailseite_lehrerView(request):
    subjects = Subject.objects.filter(unterricht__Teacher = request.user)

    return render(request, 'noten/detailseite_lehrer.html', {'latest_subject_list' : subjects})


class startseite_schuelerView(LoginRequiredMixin, generic.ListView):
    model = Student
    template_name = 'noten/startseite_schueler.html'

    def get_queryset(self):
        return "test"


@login_required
def startseite_lehrer(request):
    klassen = Klasse.objects.filter(unterricht__Teacher=request.user)

    return render(request , 'noten/startseite_lehrer.html', {'latest_klasse_list' : klassen})

@login_required
def startseite_schueler(request):
    subjects = Subject.objects.all()

    return render(request, 'noten/startseite_schueler.html', {'latest_subject_list' : subjects})

@login_required
def detailseite_lehrer(request):
    subjects = Subject.object.filter(Subject__subject_name = request.user)

    return render(request, 'noten/detailseite_lehrer.html', {'latest.subject_list' : subjects})

