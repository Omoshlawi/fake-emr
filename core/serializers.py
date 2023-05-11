from rest_framework import serializers

from core.models import HealthFacility, FacilityType, MaritalStatus, AppointMentType


class HealthFacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HealthFacility
        fields = ('url', 'identification_code', 'name', 'type', 'longitude', 'latitude', 'address')
        extra_kwargs = {
            'url': {'view_name': 'facilities-detail'},
            'type': {'view_name': "types-detail"}
        }


class FacilityTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FacilityType
        fields = ('url', 'level', 'name', 'description')
        extra_kwargs = {
            'url': {'view_name': "types-detail"}
        }


class MaritalStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ('url', 'status', 'description', 'is_active', 'created_at')
        extra_kwargs = {
            'url': {'view_name': 'status-detail'}
        }


class AppointMentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppointMentType
        fields = ('url', 'appointment_code', 'type', 'description', 'created_at')
        extra_kwargs = {
            'url': {'view_name': 'appointment-types-detail'}
        }
