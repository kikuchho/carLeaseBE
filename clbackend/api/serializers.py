import math
from django.contrib.auth.models import User
from rest_framework import serializers 
from .models import BookMark, Car, Grade, Color, Interior, InteriorExteriorUpgrade, Numberplate, OptionPackage, TireUpgrade


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
        fields = ["id", "author", "plan", "contract_year", "carid", "imgname","is_upFrontFee", "grade_id", "color_id", "interior_id", 
                  "option_package_id", "option_package_listitems", "interior_exterior_upgrade_id", "tire_upgrade_id", "numberplate_number", "created_at", "updated_at"]
        extra_kwargs = {
                        "author": {"read_only": True},
                        "created_at": {"read_only": True},
                        "updated_at": {"read_only": True},
                        }

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

    #when get requsest is made, these methods will be called to calculate the paylist
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
        fields = ["id", "grade", "gasType", "wheelDrive",   "name", "car_id", "price"]
        extra_kwargs = {"id" : {"read_only": True}}

    def create(self, validated_data):
        print(validated_data)
        grade = Grade.objects.create(**validated_data)
        return grade
    
class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ["id", "color","color_hex", "subname",  "name", "car_id", "price"]
        extra_kwargs = {"id" : {"read_only": True}}

    def create(self, validated_data):
        print(validated_data)
        color = Color.objects.create(**validated_data)
        return color
    

class InteriorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interior
        fields = ["id", "interior", "interiorcolor", "seat",  "imgname" , "name", "car_id", "price"]
        extra_kwargs = {"id" : {"read_only": True}}

    def create(self, validated_data):
        print(validated_data)
        interior = Interior.objects.create(**validated_data)
        return interior
    


class OptionPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OptionPackage
        fields = ["id", "optionpackage",  "name", "title", "subtitle", "listItems" , "comment" , "car_id", "price"]
        extra_kwargs = {"id" : {"read_only": True}}  # we can implement try clause to implement 

    def create(self, validated_data):
        print(validated_data)
        optionPackage = OptionPackage.objects.create(**validated_data)
        return optionPackage

class InteriorExteriorUpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = InteriorExteriorUpgrade
        fields = ["id", "interior_exterior_upgrade","imgurl", "is_exterior", "name", "car_id",  "price"]
        extra_kwargs = {"id" : {"read_only": True}}

    def create(self, validated_data):
        print(validated_data)
        interior = InteriorExteriorUpgrade.objects.create(**validated_data)
        return interior
    
class TireUpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TireUpgrade
        fields = ["id", "tire_upgrade", "name", "title", "description", "car_id", "price"]
        extra_kwargs = {"id" : {"read_only": True}}

    def create(self, validated_data):
        print(validated_data)
        tire_upgrade = TireUpgrade.objects.create(**validated_data)
        return tire_upgrade
       

class NumberplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Numberplate
        fields = ["id", "title", "imgurl", "numberplate", "car_id", "price"]
        extra_kwargs = {"id" : {"read_only" : True}}
    
    def create(self, validated_data):
        print(validated_data )
        numberplate = Numberplate.objects.create(**validated_data)
        return numberplate
    

class CarOptionsSerializer(serializers.ModelSerializer):
    #The field names must match the related_name in your MODELS:  
    # ex)  TireUpgrades = TireUpgradeSerializer(many=True, read_only=True) -> doesn't bring any result 
    # tire_upgrades = TireUpgradeSerializer(many=True, read_only=True) -> will work
    grades = GradeSerializer(many=True, read_only=True)
    colors = ColorSerializer(many=True, read_only=True)
    interiors = InteriorSerializer(many=True, read_only=True)
    option_packages = OptionPackageSerializer(many=True, read_only=True)
    interior_exterior_upgrades = InteriorExteriorUpgradeSerializer(many=True, read_only=True)
    tire_upgrades = TireUpgradeSerializer(many=True, read_only=True)
    numberplates = NumberplateSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'name', 'price', 'grade', 'imgname', 'grades', 'colors', 'interiors', 'option_packages', 'interior_exterior_upgrades', 'tire_upgrades', 'numberplates']



    