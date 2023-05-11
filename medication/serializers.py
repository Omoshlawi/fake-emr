from rest_framework import serializers

from medication.models import AppointMent, HIVLabTest


class AppointMentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppointMent
        fields = ('url', 'patient', 'type', 'doctor', 'next_appointment_date', 'created_at', 'updated_at')
        extra_kwargs = {
            'url': {'view_name': 'appointments-detail'},
            'patient': {'view_name': 'patients-detail'},
            'type': {'view_name': 'appointment-types-detail'},
            'doctor': {'view_name': 'users-detail'},
        }


class HIVLabTestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HIVLabTest
        fields = ('url', 'appointment', 'cd4_count', 'viral_load')
        extra_kwargs = {
            'url': {'view_name': 'tests-detail'},
            'appointment': {'view_name': 'appointments-detail'},
        }
