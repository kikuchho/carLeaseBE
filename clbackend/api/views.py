from django.shortcuts import render
from django.contrib.auth.models import User 
from rest_framework import generics
from .serializers import CarSerializer, UserSerializer , BookMarkSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import BookMark
from .models import Car
#from clbackend.api import serializers


class CarListCreate(generics.ListCreateAPIView):
    #what serializer do is check if all the data is acurate 
    serializer_class = CarSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # Add this line to bypass authentication completely

    #below you are overriding methods 
    def get_queryset(self):
        return Car.objects.all()
    
    def  perform_create(self, serializer):
       
        if serializer.is_valid():
            serializer.save()

        else: 
            print(serializer.errors) 


#update 
class BookMarkUpdate(generics.UpdateAPIView):
    serializer_class = BookMarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return BookMark.objects.filter(author = user )
    
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)

        else: 
            print(serializer.errors)


class BookMarkListCreate(generics.ListCreateAPIView):
    #what serializer do is check if all the data is acurate 
    serializer_class = BookMarkSerializer
    permission_classes = [IsAuthenticated]

    #below you are overriding methods 
    def get_queryset(self):
        # Filter Bookmarks by the logged in user 
        user = self.request.user
        return BookMark.objects.filter(author=user)
    
    def  perform_create(self, serializer):
        #here, we are overriding the create function 
        #in if statment, it checks if all the data (serilizer) that was passed is valid
        #and then make a new a new bookmark by saving the serializer 
        #author=self.request.user means that the author field of the object being created 
        #will be set to the currently authenticated user who made the request.
        if serializer.is_valid():
            serializer.save(author=self.request.user)

        else: 
            print(serializer.errors)


class BookMarkDelete(generics.DestroyAPIView):
    
    serializer_class = BookMarkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user 
        return BookMark.objects.filter(author = user )


# Create your views here.
class CreateUserView(generics.CreateAPIView):
    # we get the all user objects to make sure we don't craete dulicate user
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
