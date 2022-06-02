from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)


class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE,  related_name='measurements')
    temperature = models.FloatField()
    measure_date = models.DateField(auto_now_add=True)
