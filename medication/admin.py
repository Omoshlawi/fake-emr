from django.contrib import admin

from medication.models import AppointMent


# Register your models here.


@admin.register(AppointMent)
class AppointMentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'type', 'doctor', 'next_appointment_date', 'created_at', 'updated_at')
