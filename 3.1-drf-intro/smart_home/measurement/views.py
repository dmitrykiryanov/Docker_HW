# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView

from .models import Sensor, Measurement

from .serializers import MeasurementSerializer, SensorSerializer, SensorDetailSerializer


class CreateSensorView(CreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class UpdateSensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class CreateMeasurementView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class ListSensorView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


