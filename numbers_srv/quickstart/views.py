#from django.shortcuts import renderq
# import requests
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from django.http import HttpResponse
from numbers_srv.quickstart.serializers import UserSerializer, GroupSerializer


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