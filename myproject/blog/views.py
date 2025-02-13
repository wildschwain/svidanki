from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile, Reaction, User, Match
from django.contrib import messages
import random



def User_List(request):
    if request.method == 'post':
        return render(request, 'home.html', 'user_profile.html')

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
    current_user_profile = request.user.profile
    current_user_city = current_user_profile.sity
    profiles = Profile.objects.filter(sity=current_user_city).exclude(user=request.user)
    random_profile = random.sample(list(profiles), min(len(profiles), 1))
    #----------------------------------------------------------------------------------------------
    profile_data = []
    for profile in profiles:
        love_count = profile.reaction.filter(reaction='love').count()
        dislike_count = profile.reaction.filter(reaction='dislike').count()
        profile_data.append({'profile': profile, 'love_count': love_count, 'dislike_count': dislike_count})
    #----------------------------------------------------------------------------------------------
    user_profile = get_object_or_404(Profile, user=request.user) 
    return render(request, 'home.html' , {'user_profile': user_profile , 'profiles': random_profile, 'profile_data':profile_data})


@login_required
def reaction(request, profile_id, reaction_type):
    profile = get_object_or_404(Profile, id=profile_id)
    Reaction.objects.update_or_create(
        profile=profile,
        user=request.user, 
        defaults={'reaction':reaction_type}
    )
    if reaction_type == 'love':
        other_reaction = Reaction.objects.filter(
            profile__user=request.user,
            user=profile.user,
            reaction='love'
        ).first()
        if other_reaction:
            messages.success(request, f'У вас взаимная симпатия с {profile.user.username}, начните общение!')
        else:
            messages.info(request, f'{profile.user.username} уведомлён о вашей симпатии')
    return redirect('home')



def user_profile(request, user_id):
    user = get_object_or_404(Profile, id = user_id )
    return render(request, 'user_profile.html', {'user':user})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users':users})

@login_required
def chat(request, user_id):
    other_user = get_object_or_404(User, id=user_id)
    if not Match.objects.filter(
                    user1=min(request.user, request.profile.user, key=lambda u: u.id),
                    user2=max(request.user, request.profile.user, key=lambda u: u.id),
                    is_mutual=True
                ).exists():
                return redirect('home')
    return render(request, 'chat.html', {'other_user':other_user})