from django.shortcuts import render
from number.models import Number
from django.contrib.auth.models import User, Group

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets, generics
from django.http import HttpResponse
from number.serializers import NumberSerializer, GroupSerializer, UserSerializer

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
        if value:
            queryset = Number.objects.extra(select={'d_field': 'abs({} - value)'.format(value)}).order_by('d_field')[:1]
        else: 
            queryset = Number.objects.all()
        return queryset

@api_view(['GET', 'PUT'])
def number_list(request):
    if request.method == 'GET':
        numbers = Number.objects.all()
        serializer = NumberSerializer(numbers, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer_class = NumberSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def index(request):
     r = requests.get('http://httpbin.org/status/418')
     print(r.text)
     return HttpResponse('<pre>' + r.text + '</pre>') 