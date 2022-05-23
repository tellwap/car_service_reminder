from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import CarInsuaranceSerializer, CarSerializer,CarMonitoringSerializer
from insuarances.models import Car, CarInsuarance,CarMonitoring


class CarListApiView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarCreateApiView(CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


# insuarance
class CarInsuaranceListApiView(ListAPIView):
    # queryset = CarInsuarance.objects.all()
    serializer_class = CarInsuaranceSerializer

    def get_queryset(self, *args, **kwargs):
        # queryset = Quiz.objects.all()
        car_id = self.request.GET.get('car_id')
        if car_id:
            queryset = CarInsuarance.objects.filter(car__id=car_id)
            return queryset


class CarInsuaranceCreateApiView(CreateAPIView):
    queryset = CarInsuarance.objects.all()
    serializer_class = CarInsuaranceSerializer


class CarMonitoringListApiView(ListAPIView):
    queryset = CarMonitoring.objects.all()
    serializer_class = CarMonitoringSerializer


class CarMonitoringCreateApiView(CreateAPIView):
    queryset = CarMonitoring.objects.all()
    serializer_class = CarMonitoringSerializer
