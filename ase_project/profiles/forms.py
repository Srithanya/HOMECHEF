from django import forms
from .models import Profile
from .models import SellerProfile
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField
	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['phone_number', 'image']



class SellerProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = SellerProfile
		fields = ['image']