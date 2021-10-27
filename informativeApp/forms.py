from django import forms
from django.forms import ModelForm
from .models import UserSurvey

# Create your forms here.

class ContactUs(forms.Form):
	first_name = forms.CharField(max_length = 50)
	last_name = forms.CharField(max_length = 50)
	email_address = forms.EmailField(max_length = 150)
	message = forms.CharField(widget = forms.Textarea, max_length = 2000)

class UserSurvey(ModelForm):
	class Meta:
		model = UserSurvey
		fields = "__all__"
		
