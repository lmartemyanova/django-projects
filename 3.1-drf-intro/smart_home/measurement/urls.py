from django.urls import path

from .views import SensorsView, SensorDetailsView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorDetailsView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
