from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
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

class Lesson(models.Model):
    lesson_date = models.DateTimeField(auto_now_add=True)
    plan = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.lesson_date

    class Meta:
        ordering = ['lesson_date']


