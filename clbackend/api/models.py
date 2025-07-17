from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookMark(models.Model): 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "bookmarks")
    plan = models.JSONField(default=list) #array of objects 
    contract_year = models.IntegerField()
    carid = models.IntegerField()

    def __str__(self):
        return self.author.username

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    grade = models.CharField(max_length=100, default="スタンダード")
    imgname = models.CharField(max_length=100, default="default.png")

    def __str__(self):
        return self.name 


## Additional models for car options 

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    grade = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='grades')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    
class Color(models.Model):
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='colors')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

   
class Interior(models.Model):
    id = models.AutoField(primary_key=True)
    interior = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='interiors')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class OptionPackage(models.Model):
    id = models.AutoField(primary_key=True)
    optionpackage = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='option_packages')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class InteriorExteriorUpgrade(models.Model):
    id = models.AutoField(primary_key=True)
    interior_exterior_upgrade = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='interior_exterior_upgrades')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name   