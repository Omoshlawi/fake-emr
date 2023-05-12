from rest_framework import serializers

from core.models import HealthFacility, FacilityType, MaritalStatus, AppointMentType


class HealthFacilitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HealthFacility
        fields = ('url', 'id', 'identification_code', 'name', 'type', 'longitude', 'latitude', 'address')
        extra_kwargs = {
            'url': {'view_name': 'facilities-detail'},
            'type': {'view_name': "types-detail"}
        }

    def to_representation(self, instance):
        _dict = super().to_representation(instance)
        _dict.update({
            'type': FacilityTypeSerializer(instance=instance.type, context=self.context).data
        })
        return _dict


class FacilityTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FacilityType
        fields = ('url', 'id', 'level', 'name', 'description')
        extra_kwargs = {
            'url': {'view_name': "types-detail"}
        }


class MaritalStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaritalStatus
        fields = ('url', 'id', 'status', 'description', 'is_active', 'created_at')
        extra_kwargs = {
            'url': {'view_name': 'status-detail'}
        }


class AppointMentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppointMentType
        fields = ('url', 'id', 'code', 'type', 'description', 'created_at')
        extra_kwargs = {
            'url': {'view_name': 'appointment-types-detail'}
        }
