from django.contrib import admin

# Register your models here.
from bookings.models import Lesson
from bookings.models import Student


class LessonsAdmin(admin.ModelAdmin):
    fields= ["lesson_date", "student", "notes"]

class StudentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lesson, LessonsAdmin)
admin.site.register(Student, StudentsAdmin)