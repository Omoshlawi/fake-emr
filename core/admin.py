from django.contrib import admin

from core.models import HealthFacility, FacilityType


# Register your models here.


@admin.register(HealthFacility)
class HIVClinicAdmin(admin.ModelAdmin):
    list_display = ('name', 'longitude', 'latitude', 'address')


@admin.register(FacilityType)
class FacilityTypeAdmin(admin.ModelAdmin):
    list_display = ('level', 'name')
