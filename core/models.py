from django.db import models


# Create your models here.


# Toa medical specialties, staffing, equipment, bed capacity
class FacilityType(models.Model):
    level = models.PositiveIntegerField()
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ['-level']

    def __str__(self):
        return self.name


class HealthFacility(models.Model):
    identification_code = models.CharField(max_length=50, unique=True, null=True, blank=True)
    name = models.CharField(max_length=100)
    type = models.ForeignKey(FacilityType, on_delete=models.CASCADE, related_name='facilities')
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    address = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created_at']


class MaritalStatus(models.Model):
    status = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status

    class Meta:
        ordering = ['-created_at']


class AppointMentType(models.Model):
    code = models.CharField(max_length=20, unique=True)
    type = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

    class Meta:
        ordering = ['-created_at']


