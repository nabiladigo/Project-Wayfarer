from logging import NullHandler
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=25, null=True)
    profile_pic = models.CharField(max_length=255)
    current_city = models.ForeignKey('City',null=True, on_delete=models.SET_NULL)

class Country(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250, null= True)


class City(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=250, null= True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Post(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=250, null= True)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)








    

