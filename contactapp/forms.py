from django import forms
from contactapp.models import Login
from contactapp.models import Contacts1



class Login_details(forms.Form):
    user_id_number=forms.CharField(max_length=100,required=True) #The user number serves as the number
    password = forms.CharField(widget=forms.PasswordInput())  #Password for the relevent number

class Contact_add1(forms.ModelForm):
    class Meta:
        model=Contacts1


