from django.contrib import admin
from .models import Profile, Country, City, Post, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Comment)
admin.site.register(Post)
