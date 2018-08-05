from django.contrib.auth.models import User
from userauth.models import Userprofileinfo
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','password','email')

class UserprofileinfoForm(forms.ModelForm):
    class Meta():
        model = Userprofileinfo
        fields = ('portfilio_site','portfilio_picture')