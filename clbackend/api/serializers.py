import math
from django.contrib.auth.models import User
from rest_framework import serializers 
from .models import BookMark, Car, Grade, Color, Interior, OptionPackage


# Define API in serializers.py 
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

# #bookmark.plan = [
#     {"plan_id": 1, "name": "Basic", "amount": 500},
#     {"plan_id": 2, "name": "Premium", "amount": 1000}
# ]

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
    
    
    


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ["id", "grade",  "name", "car_id", "price"]
        extra_kwargs = {"id" : {"read_only": True}}

    def create(self, validated_data):
        print(validated_data)
        grade = Grade.objects.create_user(**validated_data)
        return grade
    
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "color",  "name", "car_id", "price"]
        extra_kwargs = {"id" : {"read_only": True}}

    def create(self, validated_data):
        print(validated_data)
        color = Color.objects.create_user(**validated_data)
        return color
    

class InteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = ["id", "interior",  "name", "car_id", "price"]
        extra_kwargs = {"id" : {"read_only": True}}

    def create(self, validated_data):
        print(validated_data)
        interior = Interior.objects.create_user(**validated_data)
        return interior
    
class OptionPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionPackage
        fields = ["id", "interior",  "name", "car_id", "price"]
        extra_kwargs = {"id" : {"read_only": True}}

    def create(self, validated_data):
        print(validated_data)
        optionPackage = OptionPackage.objects.create_user(**validated_data)
        return optionPackage