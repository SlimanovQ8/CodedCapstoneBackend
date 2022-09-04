
from django import forms
from django.contrib.auth import get_user_model
from tbr3at import models


User = get_user_model()

# Register Form 
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username","password","first_name","last_name","email"]
        widgets = {
            "password": forms.PasswordInput(),
        }


# Login Form 
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())



#category form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        exclude = ["created_by"]



class itemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        exclude = ["created_by"]


#admin form
class AdminForm(forms.ModelForm):
    class Meta:
        model = models.User
        exclude = ["created_by"]