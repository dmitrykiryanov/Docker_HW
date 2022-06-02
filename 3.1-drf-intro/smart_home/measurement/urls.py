from django.urls import path

from .views import CreateSensorView, UpdateSensorView, CreateMeasurementView, ListSensorView, SensorDetailView

urlpatterns = [
    path("create_sensor/", CreateSensorView.as_view()),
    path("update_sensor/<pk>/", UpdateSensorView.as_view()),
    path("list_sensors/", ListSensorView.as_view()),
    path("measure/", CreateMeasurementView.as_view()),
    path("info_sensor/<pk>/", SensorDetailView.as_view())

]
