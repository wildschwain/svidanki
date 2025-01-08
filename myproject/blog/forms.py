from django import forms 
from .models import Task,  Profile, Sity
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#Форма не связаная с моделью
class TaskForm(forms.Form):
    title = forms.CharField(max_length=200, label="Название")
    description = forms.CharField(widget=forms.Textarea, label="Описание")
    date = forms.DateField(widget=forms.DateInput( attrs={ 'type':'date' }), label="Дата завершения")

#Форма связаная с моделью
class TaskModelForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','date']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Адрес электронной почты")

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["age", "sity" , "about_me" , "gender" , "the_purpose_of_dating", "preferences", "image"]
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'about_me': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'sity': forms.Select(attrs={'class': 'form-control'}),
        }