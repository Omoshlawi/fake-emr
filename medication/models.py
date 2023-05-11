from django.db import models


# Create your models here.

class AppointMent(models.Model):
    patient = models.ForeignKey("users.Patient", related_name='appointments', on_delete=models.CASCADE)
    type = models.ForeignKey('core.AppointMentType', related_name='appointments', on_delete=models.CASCADE)
    doctor = models.ForeignKey('auth.User', related_name='appoints', on_delete=models.CASCADE, )
    next_appointment_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doctor} appointment to {self.patient}"

    class Meta:
        ordering = ['-created_at']


class HIVLabTest(models.Model):
    appointment = models.ForeignKey(AppointMent, related_name='test', on_delete=models.CASCADE)
    cd4_count = models.PositiveIntegerField()
    viral_load = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.patient} lab HIV test"

    class Meta:
        ordering = ['-appointment__created_at']
