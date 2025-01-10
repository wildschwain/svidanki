from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile, Sity, User
import random
from random import random



def User_List(request):
    if request.method == 'post':
        return render(request, 'home.html', 'user_profile.html')

def Home(request):
    if request.method == "POST":
        return render(request, 'home.html')

def Alina(request):
    if request.method == "POST":
        return render(request, 'alina.html')
    
def register(request):
    if request.method=="POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form' : form})

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Укажите имя URL
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
    
@login_required
def profile(request):
    if request.method == 'POST':
        forms = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if forms.is_valid():
            forms.save()
            return redirect('profile')
    else:
        forms = ProfileForm(instance=request.user.profile)
    return render(request, 'profile.html', {'form': forms})

def home(request):
    user_profile = get_object_or_404(Profile, user=request.user) 
    return render(request, 'home.html' , {'user_profile': user_profile})



def user_profile(request, user_id):
    user = get_object_or_404(Profile, id = user_id )
    return render(request, 'user_profile.html', {'user':user})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users':users})