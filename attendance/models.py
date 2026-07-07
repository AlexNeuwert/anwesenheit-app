from django.db import models
from django.utils.timezone import now


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_class = models.CharField(max_length=10)


    note = models.TextField(blank=True)


    def __str__(self):
        return self.name



class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.check_in}"
    





