from django.urls import path
from .views import CarListApiView, CarCreateApiView, CarInsuaranceListApiView, CarInsuaranceCreateApiView, \
    CarMonitoringListApiView,CarMonitoringCreateApiView, CarMonitoringViewSet

urlpatterns = [
    path('cars', CarListApiView.as_view()),
    path('cars/create', CarCreateApiView.as_view()),

    # insuarance
    path('', CarInsuaranceListApiView.as_view()),
    path('create', CarInsuaranceCreateApiView.as_view()),
    path('monitoring', CarMonitoringListApiView.as_view()),
    path('monitoring/create', CarMonitoringCreateApiView.as_view()),
    
    path('monitoring/delete',  CarMonitoringViewSet.as_view({'get': 'list'})),

]
