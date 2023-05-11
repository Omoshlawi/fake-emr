from django.contrib import admin

# Register your models here.

from django.contrib import admin

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
        PatientTriadInline
    ]


@admin.register(Triad)
class TriadAdmin(admin.ModelAdmin):
    list_display = ('patient', 'weight', 'height', 'blood_pressure', 'created_at')
