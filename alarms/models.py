from django.db import models

from measurements.models import Measurement

class Alarm(models.Model):
    name = models.CharField(max_length=128)
    measurements = models.ManyToManyField(Measurement)

    def __str__(self) -> str:
        return '%s %s' % (self.name, self.measurements)