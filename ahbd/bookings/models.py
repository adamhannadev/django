from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    first_name = models.CharField(max_length=42)
    last_name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    created_at = models.DateTimeField(auto_now_add=True)

    def full_name(self):
        return last_name

    class Meta:
        ordering = ['last_name']
        
    def __str__(self):
        return self.last_name

class Teacher(Person):
    pass

class Student(Person):
    main_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

class Lesson(models.Model):
    lesson_date = models.DateTimeField()
    duration = models.IntegerField(default=60)
    notes = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return str(f"{self.student} - {self.lesson_date.date()} @ {self.lesson_date.time()}" )

    class Meta:
        ordering = ['lesson_date']


