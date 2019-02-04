from django.shortcuts import render

from rest_framework import viewsets
from django.http import HttpResponse
from number.serializers import NumberSerializer

# Create your views here.
class NumberViewSet(viewsets.ModelViewSet, value=0.99):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Number.objects.extra(select={'d_field': '{} - value'.format(value)}).filter(value__range=(value-100,value+100)).order_by('d_field')[:1]
    serializer_class = NumberSerializer