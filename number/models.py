import datetime

from django.db import models
from django.utils import timezone

# Create your models here.


class Number(models.Model):
    value = models.DecimalField(max_digits=999, decimal_places=2)
    description_text = models.CharField(max_length=500)
    unit = models.CharField(max_length=10)
    pub_date = models.DateTimeField('Date published', default=timezone.now)
    link = models.URLField('Url', default='#')
    poll = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return '{} - {}{}'.format(self.description_text, self.value, self.unit)

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def poll_plus(self):
        self.poll += 1
        self.save()
        return self.poll

    def poll_minus(self):
        self.poll -= 1
        self.save()
        return self.poll
