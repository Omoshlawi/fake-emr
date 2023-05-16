from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.generics import get_object_or_404
from rest_framework.reverse import reverse

from core.serializers import AppointMentTypeSerializer
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
    # patient_ccc_number = serializers.CharField(max_length=20, write_only=True)
    previous_appointment = serializers.IntegerField(write_only=True)

    class Meta:
        model = AppointMent
        fields = (
            'url', 'id',
            # 'patient_ccc_number',
            'previous_appointment',
            'patient', 'type', 'doctor', 'tests', 'next_appointment_date',
            'created_at', 'updated_at'
        )
        extra_kwargs = {
            'url': {'view_name': 'appointments-detail'},
            'patient': {'view_name': 'patients-detail', 'read_only': True},
            'type': {'view_name': 'appointment-types-detail', 'read_only': True},
            'doctor': {'view_name': 'users-detail', 'read_only': True},
        }

    # def validate_patient_ccc_number(self, patient_ccc_number):
    #     from users.models import Patient
    #     try:
    #         Patient.objects.get(patient_number=patient_ccc_number)
    #     except Patient.DoesNotExist:
    #         raise ValidationError("No patient with such cc number")

    def validate_previous_appointment(self, previous_appointment):
        try:
            AppointMent.objects.get(id=previous_appointment)
        except AppointMent.DoesNotExist:
            raise ValidationError("No appointment with search Id")
        return previous_appointment

    def create(self, validated_data):
        print(validated_data)
        # from users.models import Patient
        # patient = get_object_or_404(Patient, patient_number=validated_data.pop("patient_ccc_number"))
        prev = get_object_or_404(AppointMent, id=validated_data.pop("previous_appointment"))
        validated_data.update({
            'patient': prev.patient,
            'type': prev.type,
            'doctor': prev.doctor,
        })
        return super().create(validated_data)

    def to_representation(self, instance):
        from users.serializers import UserSerializer
        _dict = super().to_representation(instance)
        tests = _dict.pop("tests")
        _dict.update({
            'type': AppointMentTypeSerializer(instance=instance.type, context=self.context).data,
            'doctor': UserSerializer(instance=instance.doctor, context=self.context).data,
            'tests': {
                'count': len(tests),
                'url': reverse(
                    viewname='tests-list',
                    request=self.context.get('request')
                ),
                'list': tests
            }
        })

        return _dict


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
        from users.serializers import UserSerializer
        _dict = super().to_representation(instance)
        _dict.update({
            'doctor': UserSerializer(instance=instance.doctor, context=self.context).data,
            'regimen': ARTRegimenSerializer(
                instance=instance.regimen,
                context=self.context
            ).data if instance.regimen else None
        })
        return _dict
