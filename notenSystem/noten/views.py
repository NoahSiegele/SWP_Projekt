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

class startseite_schuelerView(LoginRequiredMixin, generic.ListView):
    model = Student
    template_name = 'noten/startseite_schueler.html'

    def get_queryset(self):
        return "test"


@login_required
def startseite_lehrer(request):
    klassen = Klasse.objects.filter(unterricht__Teacher=request.user).distinct()

    return render(request , 'noten/startseite_lehrer.html', {'latest_klasse_list' : klassen})

@login_required
def startseite_schueler(request):
    subjects = Subject.objects.all()

    return render(request, 'noten/startseite_schueler.html', {'latest_subject_list' : subjects})

@login_required
def detailseite_lehrer(request, klasse_id):
    subjects = Subject.objects.filter(unterricht__Teacher=request.user, unterricht__Klasse__id = klasse_id)

    return render(request, 'noten/detailseite_lehrer.html', {'latest_subject_list' : subjects})

@login_required
def detailseite_schueler(request, subject_id):
    noten = Note.objects.filter(Student__user = request.user, Unterricht_id=subject_id)

    return render(request, 'noten/detailseite_schueler.html', {'latest_noten_liste' : noten})

@login_required
def detailseite_notenvergebung_lehrer(request, klasse_noten_id):
    notenvergebung = Student.objects.all()

    return render(request, 'noten/detailseite_notenvergebung_lehrer.html', {'latest_student_list' : notenvergebung, 'klasse_noten_id' : klasse_noten_id})

@login_required
def noteneintragung_lehrer(request, klasse_noten_id):
    noteneintragung = Student.objects.all()

    return render(request, 'noten/noteneintragung_lehrer.html')