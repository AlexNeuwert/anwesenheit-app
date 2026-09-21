
from django.contrib import admin
from .models import Student, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
        "student_id",
        "student_class",
    ]


admin.site.register(Attendance)




