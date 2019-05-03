from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True,help_text='Enter your first name.')
    last_name = forms.CharField(max_length=30,required=True,help_text='Enter your last name.')
    email = forms.EmailField(max_length=254, help_text='Enter your Email address.')
    CHOICES = (('Option 1', 'إدارة سوهاج'),('Option 2', 'إدارة قنا'),)
    Adminstration = forms.ChoiceField(choices=CHOICES)

    class Meta:

        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2','Adminstration' ]

class SuggestionForm(forms.ModelForm):

    class Meta:
        model = Suggestion
        fields = ['suggestion_title','suggestion_kind','suggestion_writer','suggestion_email','suggestion_content',]


class ComplaintForm(forms.ModelForm):

    class Meta:
        model = Complaint
        fields = ['Complaint_title','Complaint_writer','Complaint_writer_id','Complaint_writer_phone','Complaint_email','Complaint_content']