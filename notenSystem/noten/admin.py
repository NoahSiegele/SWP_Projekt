from django.contrib import admin

from .models import Student, Subject, Unterricht, Klasse, Note

admin.site.register(Klasse)
admin.site.register(Subject)
admin.site.register(Unterricht)
admin.site.register(Student)
admin.site.register(Note)

