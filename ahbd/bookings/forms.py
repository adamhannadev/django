from django import forms
from bookings.models import Student, Teacher

students = Student.objects.all()
teachers = Teacher.objects.all()

class LessonForm(forms.Form):
    lesson_date = forms.DateTimeField()
    duration = forms.DurationField()
    student = forms.ModelChoiceField()