from django.contrib.auth.models import User
from rest_framework import serializers 

class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def craete(self, validated_data):
        user = User.objects.craete_user(**validated_data)
        return user
    
    