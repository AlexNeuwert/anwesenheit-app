"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from attendance import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard),   # ✅ DAS ist neu
    path('scan/<int:student_id>/', views.scan_student),
    path('status/', views.get_status),
    path('scan-page/', views.scanner_page),
    path('qr/<int:student_id>/', views.generate_qr),
    path('import/', views.import_students),
    path('export-qr/', views.export_qr),
    path('export_excel/', views.export_excel),
    path('monat/', views.monthly_report),
    path('monat/', views.monthly_overview),
    path('edit/<int:attendance_id>/', views.edit_attendance, name='edit_attendance'),
]
