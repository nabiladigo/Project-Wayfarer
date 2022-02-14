from logging import NullHandler
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.CharField(max_length=255)
    current_city = models.ForeignKey('City',on_delete=models.SET_NULL)

class Country(models.Model):
    name = models.CharField(max_length=100)


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Post(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)








    

