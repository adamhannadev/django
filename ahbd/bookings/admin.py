from django.contrib import admin

# Register your models here.
from bookings.models import Lesson
from bookings.models import Student
from bookings.models import Teacher

class LessonsAdmin(admin.ModelAdmin):
    fields= ["lesson_date", "student", "teacher", "duration"]

class StudentsAdmin(admin.ModelAdmin):
    pass

class TeachersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Lesson, LessonsAdmin)
admin.site.register(Student, StudentsAdmin)
admin.site.register(Teacher, TeachersAdmin)