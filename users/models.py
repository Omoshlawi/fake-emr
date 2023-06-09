from django.db import models
from django.db.models import Avg, Max, Min, Count, StdDev
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

GENDER_CHOICES = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other')
)


class Patient(models.Model):
    patient_number = models.CharField(max_length=50, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    marital_status = models.ForeignKey(
        "core.MaritalStatus", on_delete=models.CASCADE,
        related_name='patients', null=True, blank=True
    )
    base_clinic = models.ForeignKey(
        "core.HealthFacility", on_delete=models.CASCADE,
        null=True, blank=True, related_name='patients'
    )
    national_id = models.PositiveIntegerField(unique=True, null=True, blank=True)
    county_of_residence = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    @property
    def age(self):
        if self.date_of_birth:
            today = timezone.now().today()
            age = today.year - self.date_of_birth.year
            # if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            #     age -= 1
            return age
        return None

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ['-created_at']


class Triad(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='triads')
    weight = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    height = models.DecimalField(decimal_places=2, max_digits=12)
    temperature = models.PositiveIntegerField(null=True, blank=True)
    heart_rate = models.PositiveIntegerField(null=True, blank=True)
    blood_pressure = models.DecimalField(decimal_places=2, max_digits=12, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']


class PatientNextOfKeen(models.Model):
    patient = models.ForeignKey(Patient, related_name='next_of_keen', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    relationship = models.CharField(max_length=100)
    address = models.CharField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


@receiver(post_save, sender=Patient)
def notify_subscribers(sender, instance, created, **kwargs):
    """Check for patient point to see if he/she is eligible for moving to next program"""
