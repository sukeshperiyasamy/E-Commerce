from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class CustomUserForm(UserCreationForm):#It will Inherits an UserCreationFrom from Django
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the UserName'}))#attrs are the Attributes Short Form
    email=forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the E-mail'}))#attrs are the Attributes Short Form
    mob=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter the Mob-Num'}),min_length=2)#attrs are the Attributes Short Form
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter the Password'}))#attrs are the Attributes Short Form
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Retype The Password'}))#attrs are the Attributes Short Form
    class Meta:
        model=User
        fields=['username','email','mob','password1','password2']


