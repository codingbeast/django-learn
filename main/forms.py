
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput,EmailInput,PasswordInput

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    num = forms.IntegerField(required=False,help_text='optional.',widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : "Mobile Number"}))
    name = forms.CharField(required=False,help_text='optional.',widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : "Name"}))
    surname = forms.CharField(required=False,help_text='optional.',widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : "Surname"}))
    Age = forms.IntegerField(required=False,help_text='optional.',widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : "Age"}))
    Address = forms.CharField(required=False,help_text='optional.',widget=forms.TextInput(attrs={'class': 'form-control','placeholder' : "address"}))
    class Meta:
        model = User
        fields = ('username', 'num', 'name', 'surname', 'Age', 'Address', 'password1', 'password2', )

        widgets = {
            'username': TextInput(attrs={'class': 'form-control','placeholder': 'Username'}),
            }