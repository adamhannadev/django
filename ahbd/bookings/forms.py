from django import forms


class BookingForm(forms.Form):
    lesson_date = forms.DateTimeField(label="Lesson Date")
    duration = forms.IntegerField(label="Duration")
    notes = forms.TextField(label="Notes")
    student = forms.ForeignKey(Student, on_delete=forms.CASCADE, label="Student")
    teacher = forms.ForeignKey(Teacher, on_delete=forms.CASCADE, label="Teacher")