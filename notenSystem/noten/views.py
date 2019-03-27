from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.contrib.auth import logout

from .models import Klasse, Student, Test, Subject, Prüfung, Note, Unterricht, User

class IndexView(generic.ListView):
    template_name = 'registration/login.html'

    def get_queryset(self):
        return "test"

@login_required
def logout_view(request):
    logout(request)

    return render(request, 'registration/logout1.html')

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

@login_required
def startseite_lehrer(request):
    klassen = Klasse.objects.filter(unterricht__Teacher=request.user).distinct()

    return render(request , 'noten/startseite_lehrer.html', {'latest_klasse_list' : klassen})

@login_required
def startseite_schueler(request):
    subjects = Unterricht.objects.filter(Klasse__student__user = request.user)

    return render(request, 'noten/startseite_schueler.html', {'latest_subject_list' : subjects})

@login_required
def detailseite_lehrer(request, klasse_id):
    unterricht = Unterricht.objects.filter(Teacher=request.user, Klasse__id = klasse_id)
    return render(request, 'noten/detailseite_lehrer.html', {'latest_unterricht_list' : unterricht})

@login_required
def detailseite_schueler(request, subject_id):
    noten = Note.objects.filter(Student__user = request.user, Unterricht__id=subject_id)

    return render(request, 'noten/detailseite_schueler.html', {'latest_noten_liste' : noten})

@login_required
def detailseite_notenvergebung_lehrer(request, klasse_noten_id):
    notenvergebung = Student.objects.filter(klasse__unterricht__id= klasse_noten_id)

    return render(request, 'noten/detailseite_notenvergebung_lehrer.html', {'latest_student_list' : notenvergebung, 'klasse_noten_id' : klasse_noten_id})

@login_required
def noteneintragung_lehrer(request, klasse_noten_id, student_id):
    noteneintragung = Student.objects.all()
    noten = Note.objects.filter(Student= Student.objects.get(pk=student_id))

    return render(request, 'noten/noteneintragung_lehrer.html', {'subject_id': klasse_noten_id, 'student_id': student_id, 'latest_noten_list' : noten})


@login_required
def note_eintragen(request, subject_id, student_id):
    if request.POST:
        name = request.POST['examname']
        note = request.POST['note']
        student = Student.objects.get(pk=student_id)
        n = Note(Unterricht=Unterricht.objects.get(pk=subject_id), Student=student, note=note, type=name)
        n.save()
        return HttpResponseRedirect(reverse('noten:noteneintragung_lehrer', args=(subject_id, student_id, )))



#class detailseite_lehrerView(LoginRequiredMixin, generic.ListView):
 #   model = Student
  #  template_name = 'noten/detailseite_lehrer.html'
#
 #   def get_queryset(self):
  #      return "test"
#
#class startseite_schuelerView(LoginRequiredMixin, generic.ListView):
 #   model = Student
  #  template_name = 'noten/startseite_schueler.html'

   # def get_queryset(self):
    #    return "test"