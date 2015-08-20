from django import forms 
from django.core.validators import RegexValidator
from maim.models import WebUser, Picture
from django.contrib.auth.models import User


class CreateUser(forms.ModelForm):
	password = forms.CharField(required=True, widget=forms.PasswordInput())
	username = forms.CharField(help_text=' Letters Only')
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name',  'password','email']
		


# class Signup(forms.Form):
# 	letter_val = RegexValidator(r'^[a-zA-z]*$', 'Please Type Letters')
# 	name = forms.CharField(required=True, validators=[letter_val])
# 	email = forms.CharField(required=True)
# 	password = forms.CharField(widget= forms.PasswordInput(), required=True)


class Login(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(required=True, widget=forms.PasswordInput())



class UploadImage(forms.ModelForm):
	class Meta:
		model = Picture
		fields = '__all__'

	# image = forms.ImageField(required=True)
	# country = forms.CharField(required=True)
	# city = forms.CharField()



# class SearchUser(forms.Form):
# 	username = forms.CharField()
# 	first_name = forms.CharField()


# class Update(forms.Form):
