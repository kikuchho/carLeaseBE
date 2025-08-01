from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookMark(models.Model): 
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "bookmarks")
    plan = models.JSONField(default=list) #array of objects 
    contract_year = models.IntegerField()

    carid = models.IntegerField()
    imgname = models.CharField(max_length=100, default="default.png")  # Default image name if not selected
    # Foreign keys to other models, default to 0 if not selected
    is_upFrontFee = models.BooleanField(default=False)  # True if upfront fee is selected, False if not
    grade_id = models.IntegerField(default=0)  # ForeignKey to Grade model
    color_id = models.IntegerField(default=0)  # ForeignKey to Color model
    interior_id = models.IntegerField(default=0)  # ForeignKey to Interior model
    option_package_id = models.IntegerField(default=0)  # ForeignKey to OptionPackage model
    option_package_listitems = models.JSONField(default=list)  # List of selected items in the option package
    interior_exterior_upgrade_id = models.IntegerField(default=0)  # ForeignKey to InteriorExteriorUpgrade model
    tire_upgrade_id = models.IntegerField(default=0)  # ForeignKey to TireUpgrade model
    numberplate_number = models.CharField(max_length=100, default="")  # Number plate number

    created_at = models.DateTimeField(auto_now_add=True )
    updated_at = models.DateTimeField(auto_now=True)

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
    gasType = models.CharField(max_length=100, default="ガソリン")
    wheelDrive = models.CharField(max_length=100, default="2WD")
    name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='grades')
    #extra fee the customer has to pay for the grade upgrade
    price = models.IntegerField(default=0)

    # This method returns the string representation of the model instance 
    # in this case , if you access the url the name "ヤリス,　ライズ" will be displayed
    # if you change it to self.id the PK number of Car model will be displayed
    def __str__(self):
        return self.name

    
class Color(models.Model):
    id = models.AutoField(primary_key=True)
    color = models.CharField(max_length=100)
    color_hex = models.CharField(max_length=7, default="#FFFFFF")  # Hex color code
    subname = models.CharField(max_length=100, default="標準色")
    name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='colors')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

   
class Interior(models.Model):
    id = models.AutoField(primary_key=True)
    interior = models.CharField(max_length=100)
    interiorcolor = models.CharField(max_length=100, default="ブラック")
    seat = models.CharField(max_length=100, default="ファブリック･ブラック")
    name = models.CharField(max_length=100)
    imgname = models.CharField(max_length=100, default="default_interior.png")
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='interiors')
    #extra price the customer has to pay for the interior upgrade
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class OptionPackage(models.Model):
    id = models.AutoField(primary_key=True)
    optionpackage = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default="オプションパッケージ")
    subtitle = models.JSONField(default=list )
    listItems = models.JSONField(default=list) #store image url and text for each item
    comment = models.CharField(max_length=100, default="") #ex おすすめ
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='option_packages')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    


    
class InteriorExteriorUpgrade(models.Model):
    id = models.AutoField(primary_key=True)
    interior_exterior_upgrade = models.CharField(max_length=100)
    imgurl = models.CharField(max_length=255, default="default_upgrade.png")  # URL for the image
    is_exterior = models.BooleanField(default=False)  # True if it's an exterior upgrade, False if interior
    name = models.CharField(max_length=100)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='interior_exterior_upgrades')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name   


class TireUpgrade(models.Model):
    id = models.AutoField(primary_key=True)
    tire_upgrade = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default="寒冷地仕様")
    description = models.CharField(max_length=255, default="※上記オプション以外をご希望のお客様は取扱い販売店にお問合せください")
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='tire_upgrades')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Numberplate(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    imgurl = models.CharField(max_length=100, default="default_numberplate.png")  # URL for the image
    numberplate = models.CharField(max_length=100, default="")
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='numberplates')
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.name