from django.urls import path

from . import views

from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


app_name = 'noten'
urlpatterns = [
    path('', views.index, name='index'),
    path('startseite_lehrer/', views.startseite_lehrer, name='startseite_lehrer'),
    path('startseite_schueler/', views.startseite_schuelerView.as_view(), name='startseite_schueler'),
    url(r'^admin/', admin.site.urls),
]
