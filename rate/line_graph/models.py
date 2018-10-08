from django.db import models


# Create your models here.
class RateData(models.Model):
    id = models.AutoField(primary_key=True)
    rate = models.FloatField(null=False, blank=False)
    datetime = models.DateTimeField(blank=False)

    def __str__(self):
        return str(self.rate)
