from django.urls import path

from . import views

app_name = 'noten'
urlpatterns = [
    path('', views.startseite_lehrerView.as_view(), name='startseite_lehrer'),
    path('/signup/', views.SignupView.as_view(), name='signupSeite'),
    path('/startseite_schueler/', views.startseite_schuelerView.as_view(), name='startseite_schueler')
]
