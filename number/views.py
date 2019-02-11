from django.shortcuts import render
from number.models import Number
from rest_framework import viewsets, generics
from django.http import HttpResponse
from number.serializers import NumberSerializer

# Create your views here.
class NumberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #value =1000# self.request.query_params.get('value', None)
    #queryset = Number.objects.extra(select={'d_field': '{} - value'.format(value)}).filter(value__range=(value-100,value+100)).order_by('d_field')
    serializer_class = NumberSerializer
    
    def get_queryset(self):
        value = self.request.query_params.get('value', None)
        if value == None:
            queryset = Number.objects.all()
        else: 
            queryset = Number.objects.extra(select={'d_field': 'abs({} - value)'.format(value)}).order_by('d_field')[:1]
        return queryset

# Create your views here.
class NumberList(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = NumberSerializer
    
    def get_queryset(self):
        value = self.request.query_params.get('value', None)
        queryset = Number.objects.extra(select={'d_field': '{} - value'.format(value)}).order_by('d_field')[:3]
        return queryset
