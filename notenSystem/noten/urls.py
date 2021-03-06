from django.urls import path

from . import views

from django.conf.urls import url
from django.contrib import admin


app_name = 'noten'
urlpatterns = [
    path('', views.index, name='IndexView'),
    path('logout/', views.logout_view, name='logout_view'),
    path('startseite_lehrer/', views.startseite_lehrer, name='startseite_lehrer'),
    path('startseite_schueler/', views.startseite_schueler, name='startseite_schueler'),
    path('<int:klasse_id>/detailseite_lehrer/', views.detailseite_lehrer,name='detailseite_lehrer'),
    path('<int:klasse_noten_id>/detailseite__lehrer', views.detailseite_notenvergebung_lehrer, name='detailseite_notenvergebung_lehrer'),
    path('<int:subject_id>/detailseite_schueler/', views.detailseite_schueler, name='detailseite_schueler'),
    path('<int:klasse_noten_id>/noteneintragung_lehrer/<int:student_id>', views.noteneintragung_lehrer, name="noteneintragung_lehrer"),
    path('<int:subject_id>/noteneintragung_lehrer/<int:student_id>/eintragen', views.note_eintragen, name="noten_eintragen"),
    url(r'^admin/', admin.site.urls),
]