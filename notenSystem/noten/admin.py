from django.contrib import admin

from .models import Student, Test, Prüfung, Subject, Unterricht, Klasse, Note

admin.site.register(Student)
admin.site.register(Test)
admin.site.register(Prüfung)
admin.site.register(Subject)
admin.site.register(Unterricht)
admin.site.register(Klasse)
admin.site.register(Note)

