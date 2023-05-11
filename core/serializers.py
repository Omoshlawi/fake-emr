from rest_framework import serializers

from core.models import HealthFacility, FacilityType


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
