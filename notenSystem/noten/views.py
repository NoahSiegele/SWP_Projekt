from django.views import generic


class IndexView(generic.ListView):
    template_name = 'noten/startseite_lehrer.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return "test"


class LoginView(generic.ListView):
    template_name = 'noten/loginseite.html'

    def get_queryset(self):
        return "test"
