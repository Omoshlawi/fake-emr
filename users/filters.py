from django_filters.rest_framework import filterset

from users.models import Patient


# class PatientFilterSet(filterset.FilterSet):
#     class Meta:
#         model = Patient
#         fields = ("patient_number", "national_id")
