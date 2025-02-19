from django import forms 
from .models import Profile, Sity
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Адрес электронной почты")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "age", "sity" , "about_me" , "gender" , "the_purpose_of_dating", "preferences", "message"]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'about_me': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'sity': forms.Select(attrs={'class': 'form-control'}),
        }