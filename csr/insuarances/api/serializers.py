from rest_framework.serializers import ModelSerializer,SerializerMethodField
from insuarances.models import Car, CarInsuarance,CarMonitoring


class CarSerializer(ModelSerializer):
    total_mileage = SerializerMethodField()

    class Meta:
        model = Car
        fields = ('id', 'name', 'plate_no','created_at', 'total_mileage')

    def get_total_mileage(self, obj):

        carM = CarMonitoring.objects.filter(car=obj.pk)
        totalMilleage = 0

        for mileage in carM:
            totalMilleage += mileage.distance
            print(mileage.distance)
        return totalMilleage




class CarInsuaranceSerializer(ModelSerializer):
    class Meta:
        model = CarInsuarance
        fields = ('id', 'car', 'name', 'expire_date')

class CarMonitoringSerializer(ModelSerializer):
    class Meta:
        model = CarMonitoring
        fields = ('id', 'car', 'distance','speed')