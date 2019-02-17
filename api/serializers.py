
from django.contrib.auth.models import User, Group
from number.models import Number
from rest_framework import serializers


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Number
        fields = '__all__'
        
   
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
