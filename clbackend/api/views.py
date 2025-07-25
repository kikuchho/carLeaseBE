from django.shortcuts import render
from django.contrib.auth.models import User 
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import CarSerializer, ColorSerializer, GradeSerializer, InteriorExteriorUpgradeSerializer, InteriorSerializer, NumberplateSerializer, OptionPackageSerializer, TireUpgradeSerializer, UserSerializer , BookMarkSerializer, CarPaymentSerializer, CarOptionsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import BookMark, InteriorExteriorUpgrade, Numberplate, TireUpgrade
from .models import Car, Grade, Color, Interior, OptionPackage
import math
import requests
from rest_framework import status


# Provide API to URL.py 


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

    #get request
    def get_queryset(self):
        return Car.objects.all()
    
    #post request 
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




#views for car options api

class GradeListCreate(generics.ListCreateAPIView):
    serializer_class = GradeSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # Add this line to bypass authentication completely

    #get request 
    def get_queryset(self):
        return Grade.objects.all()
    
    #post request
    def  perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

        else: 
            print(serializer.errors)


class ColorListCreate(generics.ListCreateAPIView):
    serializer_class = ColorSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # Add this line to bypass authentication completely

    # def get_queryset(self):
    #     user = self.request.user
    #     return BookMark.objects.filter(author = user )
    #get request 
    def get_queryset(self):
        thecar_id = self.kwargs.get('pk')

        if thecar_id is None:
            return Color.objects.all()
        
        return Color.objects.filter(car_id = thecar_id)
    
    #post request
    def  perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

        else: 
            print(serializer.errors)

class InteriorListCreate(generics.ListCreateAPIView):
    serializer_class = InteriorSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # Add this line to bypass authentication completely

    #get request 
    def get_queryset(self):
        return Interior.objects.all()
    
    #post request
    def  perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

        else: 
            print(serializer.errors)

class OptionPackageListCreate(generics.ListCreateAPIView):
    serializer_class = OptionPackageSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # Add this line to bypass authentication completely

    #get request 
    def get_queryset(self):
        return OptionPackage.objects.all()
    
    #post request
    def  perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

        else: 
            print(serializer.errors)

class OptionPackageUpdate(generics.UpdateAPIView):
    serializer_class = OptionPackageSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        # thecarid = self.kwargs.get('pk')
        # return OptionPackage.objects.filter(car_id = thecarid)
        # The pk in the URL will automatically filter to the specific OptionPackage
        return OptionPackage.objects.all()
    
    def perform_update(self, serializer):
        if serializer.is_valid():
            serializer.save()
            
        else: 
            print(serializer.errors)




class InteriorExteriorUpgradeListCreate(generics.ListCreateAPIView):
    serializer_class = InteriorExteriorUpgradeSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # Add this line to bypass authentication completely

    #get request 
    def get_queryset(self):
        return InteriorExteriorUpgrade.objects.all()
    
    #post request
    def  perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

        else: 
            print(serializer.errors)

class TireUpgradeListCreate(generics.ListCreateAPIView):
    serializer_class = TireUpgradeSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # Add this line to bypass authentication completely

    #get request 
    def get_queryset(self):
        return TireUpgrade.objects.all()
    
    #post request
    def  perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

        else: 
            print(serializer.errors)



class NumberplateListCreate(generics.ListCreateAPIView):
    serializer_class = NumberplateSerializer
    permission_classes = [AllowAny]
    authentication_classes = []  # Add this line to bypass authentication completely
    #get request
    def get_queryset(self):
        return Numberplate.objects.all()
    #post request
    def  perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()

        else: 
            print(serializer.errors)


class CarOptionsDetail(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarOptionsSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

    #get request
    def get_queryset(self):
        return Car.objects.all()



#this use external API to get corporate information
@api_view(['GET'])
@permission_classes([AllowAny])
def get_corporate_info(request, corporate_number):
    """
    Proxy endpoint to fetch corporate information from Japanese hojin API
    """
    try:
        # Make request to the external API
        external_url = f"https://info.gbiz.go.jp/hojin/v1/hojin/{corporate_number}"
        headers = {
            'accept': 'application/json',
            'X-hojinInfo-api-token': 'gO2vJSBxqcuR6jkvUbUy6lRqEe9dskV9'
        }
        
        response = requests.get(external_url, headers=headers)
        
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Failed to fetch corporate information', 'status': response.status_code},
                status=response.status_code
            )
            


    except requests.exceptions.RequestException as e:
        return Response(
            {'error': 'Network error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    except Exception as e:
        return Response(
            {'error': 'An unexpected error occurred', 'details': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
