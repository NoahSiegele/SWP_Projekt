from django.contrib import admin
from django.urls import path
from . import views

app_name = 'noten'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='startseite'),
]
