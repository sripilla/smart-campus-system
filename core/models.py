from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)
    year = models.IntegerField()

    class Meta:
        verbose_name_plural = "Students"

    def __str__(self):
        return self.user.username


class Faculty(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Faculty"   # ✅ FIXED

    def __str__(self):
        return self.user.username


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.BooleanField()

    class Meta:
        verbose_name_plural = "Attendance"

    def __str__(self):
        return f"{self.student} - {self.date}"


class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Assignments"

    def __str__(self):
        return self.title


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    marks = models.FloatField()

    class Meta:
        verbose_name_plural = "Marks"   # ✅ FIXED

    def __str__(self):
        return f"{self.student} - {self.subject}"