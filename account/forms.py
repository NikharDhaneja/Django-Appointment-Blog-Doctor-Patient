from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Address
from django.core.exceptions import ValidationError
from django.contrib.auth import login, authenticate

class RegistrationForm(UserCreationForm):
    ROLES = [('doctor','Doctor'),('patient','Patient')]
    role = forms.ChoiceField(choices = ROLES, widget= forms.RadioSelect)

    class Meta:
        model = User
        fields = [ "role", "first_name", "last_name", "username", "email", "profile_pic",]

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'] = forms.CharField(required=True)
        self.fields['last_name'] = forms.CharField(required=True)

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["line1", "city", "state", "pincode"]


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=30, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        user = authenticate(email=email, password=password)
        return user
