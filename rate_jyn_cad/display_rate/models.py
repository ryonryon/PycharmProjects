from django.db import models


class rateData(models.Model):
    id = models.AutoField(primary_key=True)
    rate = models.FloatField()
    datetime = models.DateTimeField()

    # def __str__(self):
    #     return str(self.rate)

