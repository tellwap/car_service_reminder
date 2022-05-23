from rest_framework.serializers import ModelSerializer
from insuarances.models import Car, CarInsuarance,CarMonitoring


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'name', 'plate_no')


class CarInsuaranceSerializer(ModelSerializer):
    class Meta:
        model = CarInsuarance
        fields = ('id', 'car', 'name', 'expire_date')

class CarMonitoringSerializer(ModelSerializer):
    class Meta:
        model = CarMonitoring
        fields = ('id', 'car', 'distance','speed')