from django.db import models


# Create your models here.
class Member(models.Model):
    name = models.CharField('Name', max_length='225')
    email = models.CharField('E-mail', max_length='225')
    age = models.IntegerField('Age', blank=False, default=0)

    def __str__(self):
        return self.name

