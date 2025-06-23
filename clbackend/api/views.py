from django.shortcuts import render
from django.contrib.auth.models import User 
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import CarSerializer, UserSerializer , BookMarkSerializer, CarPaymentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import BookMark
from .models import Car
import math
#from clbackend.api import serializers

# @api_view(['GET'])
# @permission_classes([AllowAny])
# @authentication_classes = []
# def getpaylist(request, pk):
#     try:
#         posts = Car.objects.get(id=pk) 
#         # create const for storing paylist
#         paylist1 = math.trunc(posts.price * 0.012)
#         paylist2 = math.trunc(posts.price * 0.009)
#         paylist3 = math.trunc(posts.price * 0.006)
#         paylist4 = math.trunc(posts.price * 0.003)
       
#         post_dict = {
#             "paylist1": paylist1,
#             "paylist2": paylist2,
#             "paylist3": paylist3,
#             "paylist4": paylist4
#         }
        
#         return Response(post_dict)
#     except Car.DoesNotExist:
#         return Response({"error": "Car not found"}, status=404)

class CarPaymentDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarPaymentSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # Add this line to bypass authentication completely

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
