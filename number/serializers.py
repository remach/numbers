
from django.contrib.auth.models import User, Group
from number.models import Number
from rest_framework import serializers


class NumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Number
        fields = ('value', 'description_text', 'unit')
