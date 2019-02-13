
from django.contrib.auth.models import User, Group
from number.models import Number
from rest_framework import serializers


class NumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Number
        fields = ('id','value', 'description_text', 'unit', 'link', 'pub_date')
    def create(self, validated_data):
        """
        Create and return a new `Number` instance, given the validated data.
        """
        return Number.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Number` instance, given the validated data.
        """
        instance.title = validated_data.get('value', instance.title)
        instance.code = validated_data.get('description_text', instance.code)
        instance.linenos = validated_data.get('unit', instance.linenos)
        instance.language = validated_data.get('link', instance.language)
        instance.style = validated_data.get('pub_date', instance.style)
        instance.save()
        return instance

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
