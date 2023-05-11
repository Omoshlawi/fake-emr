from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse
from rest_framework_nested import serializers as nested_serializer
from core.models import HealthFacility
from core.serializers import HealthFacilitySerializer, MaritalStatusSerializer
from users.models import PatientNextOfKeen, Patient, Triad


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')


class PatientNextOfKeenSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, instance):
        return reverse(
            viewname='patients:next-of-keen-detail',
            args=[instance.patient.id, instance.id],
            request=self.context.get('request')
        )

    class Meta:
        model = PatientNextOfKeen
        fields = ('url', 'full_name', 'address', 'phone_number', 'created_at', 'updated_at')
        extra_kwargs = {
            'url': {'view_name': 'patients:next-of-keen-detail'},
        }


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    base_clinic = serializers.HyperlinkedRelatedField(
        view_name='facilities-detail', queryset=HealthFacility.objects.all()
    )
    next_of_keen = PatientNextOfKeenSerializer(many=True, read_only=True)
    triads = nested_serializer.NestedHyperlinkedIdentityField(
        many=True, view_name='triads-detail',
        read_only=True, parent_lookup_kwargs={'patient_pk': 'patient__pk'}
    )

    def to_representation(self, instance):
        _dict = super().to_representation(instance)
        nok = _dict.pop("next_of_keen")
        nok_obj = {
            'next_of_keen': {
                'count': len(nok),
                'url': reverse(
                    viewname='next-of-keen-list',
                    args=[instance.id],
                    request=self.context.get('request')
                ),
                'list': nok
            }
        }
        base_clinic_url = _dict.pop("base_clinic")
        base_clinic_obj = {
            'base_clinic': HealthFacilitySerializer(
                instance=instance.base_clinic,
                context=self.context
            ).data
        }
        triad_list = _dict.pop('triads')
        triads_obj = {
            'triads': {
                'count': len(triad_list),
                'url': reverse(
                    viewname='triads-list',
                    args=[instance.id],
                    request=self.context.get('request')
                ),
                'url_list': triad_list
            }
        }
        marital_status = _dict.pop("marital_status")
        marital_status_obj = {
            'marital_status': MaritalStatusSerializer(
                instance=instance.marital_status,
                context=self.context
            ).data if instance.marital_status else None
        }
        _dict.update(marital_status_obj)
        _dict.update(triads_obj)
        _dict.update(nok_obj)
        _dict.update(base_clinic_obj)
        return _dict

    class Meta:
        model = Patient
        fields = (
            'url',
            'patient_number',
            'date_of_birth',
            'first_name',
            'last_name',
            'email',
            'address',
            'occupation',
            'gender',
            'phone_number',
            'marital_status',
            'county_of_residence',
            'triads',
            'patient_number',
            'next_of_keen',
            'base_clinic',
            'created_at', 'updated_at'
        )
        extra_kwargs = {
            'url': {'view_name': 'patients-detail'},
            'marital_status': {'view_name': 'status-detail'}
        }


class TriadSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, instance):
        return reverse(
            viewname='patients:triad-detail',
            args=[instance.patient.id, instance.id],
            request=self.context.get('request')
        )

    class Meta:
        model = Triad
        fields = (
            'url',
            'patient', 'weight', 'height',
            'temperature', 'heart_rate',
            'blood_pressure', 'created_at'
        )
        extra_kwargs = {
            'patient': {'view_name': 'patients:patient-detail', 'read_only': True},
        }
