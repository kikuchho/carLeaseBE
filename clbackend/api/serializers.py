import math
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
        extra_kwargs = {"author": {"read_only": True}}

class CarSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Car
        fields = ['id', 'name', 'price', 'grade', 'imgname']
        extra_kwargs = {"id" : {"read_only": True}}

class CarPaymentSerializer(serializers.ModelSerializer):
    #these fields doesn't exist in the model, but it exists in the serializer
    paylist1 = serializers.SerializerMethodField()
    paylist2 = serializers.SerializerMethodField()
    paylist3 = serializers.SerializerMethodField()
    paylist4 = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = ['id', 'name', 'price', 'grade', 'imgname', 'paylist1', 'paylist2', 'paylist3', 'paylist4']

    def get_paylist1(self, obj):
        return math.trunc(obj.price * 0.012)
    
    def get_paylist2(self, obj):
        return math.trunc(obj.price * 0.009)
    
    def get_paylist3(self, obj):
        return math.trunc(obj.price * 0.006)
    
    def get_paylist4(self, obj):
        return math.trunc(obj.price * 0.003)