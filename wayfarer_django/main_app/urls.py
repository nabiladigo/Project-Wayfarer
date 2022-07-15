from django.urls import path
from django.contrib.auth import get_user_model
from . import views,models


urlpatterns = [
    path('', views.Home.as_view(), name="home"),  
    path('about/', views.About.as_view(), name="about"),

    path('profile/<int:pk>', views.User.as_view(), name="profile"),
    path('profile/<int:pk>/posts/new/', views.PostCreate.as_view(), name="post_create"),
    path('profile/<int:pk>/update', views.UserUpdate.as_view(model=models.User), name="profile_update"),
    path('profile/<int:pk>/delete',views.UserDelete.as_view(model=models.User),name='profile_delete'),

    path('accounts/signup/', views.Signup.as_view(), name="signup"),

    path('cities/', views.CityList.as_view(), name= "city"),
    path('cities/<int:pk>/', views.CityDetail.as_view(), name= "city_detail"),

    path('posts/', views.Posts.as_view(), name="post"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update',views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>/delete',views.PostDelete.as_view(), name="post_delete"),

    path('countries/', views.CountryList.as_view(), name="country"),
    path('countries/<int:pk>/', views.CountryDetail.as_view(), name ="country_detail")
] 