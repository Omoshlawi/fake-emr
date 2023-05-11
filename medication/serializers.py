from rest_framework import serializers

from medication.models import AppointMent, HIVLabTest, ARTRegimen, PatientHivMedication


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


class ARTRegimenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ARTRegimen
        fields = ('url', 'regimen_line', 'regimen', 'created_at', 'updated_at')
        extra_kwargs = {
            'url': {'view_name': 'regimens-detail'}
        }


class PatientHivMedicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientHivMedication
        fields = ('url', 'patient', 'regimen', 'doctor', 'is_current', 'created_at', 'updated_at')
        extra_kwargs = {
            'url': {'view_name': 'hiv-prescription-detail'},
            'patient': {'view_name': 'patients-detail'},
            'regimen': {'view_name': 'regimens-detail'},
            'doctor': {'view_name': 'users-detail'},
        }
