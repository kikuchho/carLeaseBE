from django.contrib.auth.models import User
from rest_framework import serializers 
from .models import BookMark, Car

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

class BookMarkSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = BookMark
        fields = ["id", "author", "plan", "contract_year", "carid"]
        extra_kwargs = {"author": {"raed_only": True}}

class CarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Car
        fields = ["id", "name", "price"]
        extra_kwargs = {"id" : {"raed_only": True}}
