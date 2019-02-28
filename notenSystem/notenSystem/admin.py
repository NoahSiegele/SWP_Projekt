from django.contrib import admin

from .models import Teacher, Student, Subject, Noten, Klasse


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class NotenAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['Klasse', 'question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_title', 'pub_date')
    list_display = ('question_title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)