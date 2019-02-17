from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import viewsets, generics
from api.serializers import NumberSerializer, GroupSerializer, UserSerializer
from number.models import Number
from django.contrib.auth.models import User, Group
# Create your views here.


class NumberList(generics.ListCreateAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer
    
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        value = self.request.query_params.get('value', None)
        if value:
            queryset = Number.objects.extra(select={'d_field': 'abs({} - value)'.format(value),'rnd':'random()' }).filter(value__gte=float(value)*0.9,value__lte=float(value)*1.1).order_by('rnd')[:1]
        else: 
            queryset = Number.objects.all()[:7]
        return queryset
    
    def create(self, request, format=None):
        serializer = NumberSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


class NumberDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Number.objects.all()
    serializer_class = NumberSerializer


class NumberList2(APIView):
    """
    List all numbers, or create a new number.
    """
    def get(self, request, format=None):
        numbers = Number.objects.all()
        serializer = NumberSerializer(numbers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NumberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NumberDetail2(APIView): 
    def get_object(self, pk):
        try:
            return Number.objects.get(pk=pk)
        except Numbers.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        number = self.get_object(pk)
        serializer = NumberSerializer(number)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        number = self.get_object(pk)
        serializer = NumberSerializer(number, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        number = self.get_object(pk)
        number.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
       

class NumberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = NumberSerializer
    
    def get_queryset(self):
        value = self.request.query_params.get('value', None)
        if value:
            queryset = Number.objects.extra(select={'d_field': 'abs({} - value)'.format(value),'rnd':'random()' }).filter(value__gte=float(value)*0.9,value__lte=float(value)*1.1).order_by('rnd')[:1]
        else: 
            queryset = Number.objects.all()[:10]
        return queryset


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
