from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class re(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"username",
        "type":"text",
        'maxlength':'22',  
        'minlength':'4' 
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"Email",
        "type":"email"
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"phone",
        "type":"text",
        'maxlength':'22',  
        'minlength':'8' 

    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"password",
        "type":"password",
        'maxlength':'22',  
        'minlength':'8' 
    }))
    
    


    class Meta:
        model = User
        fields = ['username','email','phone','password1']

    def clean(self):
        cleaned_data = super(re, self).clean()
        password = cleaned_data.get('password1')
        phone = cleaned_data.get('phone')
        if sum(c.isdigit() for c in password) < 1:
            msg = 'Password must contain at least 1 number.'
            self.add_error('password1', msg)
        if all(c.isdigit() for c in password):
            msg = 'Your password cant be entirly numeric'
            self.add_error('password1', msg)
        if not all(c.isdigit() for c in phone):
            msg = 'Phone must contain number.'
            self.add_error('password1', msg)
        
    def __init__(self, *args, **kwargs):
        super(re, self).__init__(*args, **kwargs)
        #remove password2 
        del self.fields['password2']
class log(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"username",
        "type":"text",
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder":"password",
        "type":"password",
    }))