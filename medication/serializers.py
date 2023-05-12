from rest_framework import serializers

from medication.models import AppointMent, HIVLabTest, ARTRegimen, PatientHivMedication


class HIVLabTestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HIVLabTest
        fields = ('url', 'id', 'appointment', 'cd4_count', 'viral_load')
        extra_kwargs = {
            'url': {'view_name': 'tests-detail'},
            'appointment': {'view_name': 'appointments-detail'},
        }


class AppointMentSerializer(serializers.HyperlinkedModelSerializer):
    tests = HIVLabTestSerializer(many=True, read_only=True)

    class Meta:
        model = AppointMent
        fields = (
            'url', 'id', 'patient', 'type', 'doctor', 'tests', 'next_appointment_date',
            'created_at', 'updated_at'
        )
        extra_kwargs = {
            'url': {'view_name': 'appointments-detail'},
            'patient': {'view_name': 'patients-detail'},
            'type': {'view_name': 'appointment-types-detail'},
            'doctor': {'view_name': 'users-detail'},
        }


class ARTRegimenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ARTRegimen
        fields = ('url', 'id', 'regimen_line', 'regimen', 'created_at', 'updated_at')
        extra_kwargs = {
            'url': {'view_name': 'regimens-detail'}
        }


class PatientHivMedicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PatientHivMedication
        fields = ('url', 'id', 'patient', 'regimen', 'doctor', 'is_current', 'created_at', 'updated_at')
        extra_kwargs = {
            'url': {'view_name': 'hiv-prescription-detail'},
            'patient': {'view_name': 'patients-detail'},
            'regimen': {'view_name': 'regimens-detail'},
            'doctor': {'view_name': 'users-detail'},
        }

    def to_representation(self, instance):
        _dict = super().to_representation(instance)
        regimen = _dict.pop("regimen")
        regimen_obje = {
            'regimen': ARTRegimenSerializer(
                instance=instance.regimen,
                context=self.context
            ).data if instance.regimen else None
        }
        _dict.update(regimen_obje)
        return _dict
