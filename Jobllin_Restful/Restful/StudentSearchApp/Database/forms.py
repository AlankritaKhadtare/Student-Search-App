from django import forms
from Database.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['st_roll','st_name',
                    'st_age','st_mail',
                    'st_class','st_address']
        
        
            