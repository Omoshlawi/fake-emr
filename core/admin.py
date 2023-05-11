from django.contrib import admin

from core.models import HealthFacility, FacilityType, MaritalStatus


# Register your models here.


@admin.register(HealthFacility)
class HIVClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'longitude', 'latitude', 'address')


@admin.register(FacilityType)
class FacilityTypeAdmin(admin.ModelAdmin):
    list_display = ('level', 'name')


@admin.register(MaritalStatus)
class MaritalStatusAdmin(admin.ModelAdmin):
    list_display = ('status', 'description', 'is_active', 'created_at')
