# Register your models here.

from django.contrib import admin

from medication.admin import PatientHivMedicationInline, AppointMentInline
from .models import PatientNextOfKeen, Patient, Triad


# Register your models here.

class PatientNextOfKeenInline(admin.TabularInline):
    model = PatientNextOfKeen


class PatientTriadInline(admin.TabularInline):
    model = Triad


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('patient_number', 'base_clinic', 'created_at')
    inlines = [
        PatientNextOfKeenInline,
        PatientTriadInline,
        PatientHivMedicationInline,
        AppointMentInline
    ]


@admin.register(Triad)
class TriadAdmin(admin.ModelAdmin):
    list_display = (
        'patient', 'weight', 'height', 'blood_pressure',
        'temperature', 'heart_rate', 'created_at'
    )
    list_editable = (
        'weight', 'height', 'blood_pressure',
        'temperature', 'heart_rate'
    )
