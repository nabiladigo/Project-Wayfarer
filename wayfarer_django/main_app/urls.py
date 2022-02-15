from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),  
    path('about/', views.About.as_view(), name="about"),
    path('profile/', views.Profile.as_view(), name="profile"),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('posts/', views.Post.as_view(), name ="post"),
    path('posts/new/',  views.PostCreate.as_view(), name="post_create"),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name="post_detail"),
    path('posts/<int:pk>/update',views.PostUpdate.as_view(), name="post_update"),
    path('posts/<int:pk>/delete',views.PostDelete.as_view(), name="post_delete"),
    path('Caribbean/', views.Caribbean.as_view(), name ="caribbean"),
    path('Europe/', views.Europe.as_view(), name ="europe"),
    path('Africa/', views.Africa.as_view(), name ="africa"),
    path('Ocean/', views.Ocean.as_view(), name ="ocean"),

] 