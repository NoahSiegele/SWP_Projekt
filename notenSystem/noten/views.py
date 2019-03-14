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


class startseite_schuelerView(LoginRequiredMixin, generic.ListView):
    model = Student
    template_name = 'noten/startseite_schueler.html'

    def get_queryset(self):
        return "test"

# class startseite_lehrerView(LoginRequiredMixin, generic.ListView):
#     model = Klasse
#     template_name = 'noten/startseite_lehrer.html'
#     context_object_name = 'klasse_list'
#
#     def get_queryset(self):
#         return Student.klasse.objects.all()


@login_required
def startseite_lehrer(request):
    klassen = Klasse.objects.filter(unterricht__Teacher=request.user)

    return render(request , 'noten/startseite_lehrer.html', {'latest_klasse_list' : klassen})