from django.contrib.auth.forms import UserCreationForm, UserChangeForm, forms
from .models import User,Post

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','bio','profile_pic','current_city']

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email','username','bio','profile_pic','current_city']

    