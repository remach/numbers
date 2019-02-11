from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.
class Number(models.Model):
    value = models.DecimalField(max_digits=999, decimal_places=2)
    description_text = models.CharField(max_length=500)
    unit = models.CharField(max_length=10)
    def __str__(self):              # __unicode__ on Python 2
        return '{} - {}{}'.format( self.description_text,self.value,self.unit)
