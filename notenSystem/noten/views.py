from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


class IndexView(generic.ListView):
    template_name = 'noten/startseite_lehrer.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return "test"


def index(request):
    usergroups = request.user.groups.all()
    names = []
    for g in usergroups:
        names.append(g.name)
        if 'Teacher' in names:
            return HttpResponseRedirect('/startseite_lehrer')
        elif 'Student' in names:
            return HttpResponseRedirect('/startseite_schueler')


class startseite_schuelerView(LoginRequiredMixin,
                              generic.ListView):
    template_name = 'noten/startseite_schueler.html'

    def get_queryset(self):
        return "test"
