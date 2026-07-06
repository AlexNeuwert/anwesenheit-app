from django.db import models
from django.utils.timezone import now
class SchoolClass(models.Model):
    grade = models.IntegerField()
    section = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.grade}{self.section}"
class Student(models.Model):
    name = models.CharField(max_length=100)
    school_class = models.ForeignKey(
    SchoolClass,
    on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    check_in = models.TimeField(null=True, blank=True)
    check_out = models.TimeField(null=True, blank=True)

    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.check_in}"
    





