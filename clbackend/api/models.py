from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookMark(models.Model): 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "bookmarks")
    plan = models.IntegerField()
    contract_year = models.IntegerField()

    def __str__(self):
        return self.author.username

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.name 
    

    