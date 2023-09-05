from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.name}: {self.description}'


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Sensor id: {self.sensor}, temperature: {self.temperature}, time: {self.created_at}'
