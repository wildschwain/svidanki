from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
from .views import register

urlpatterns = [
 path('home/', views.home, name='home'),
 path('register/', views.register, name='register'),
 path('login/', LoginView.as_view(template_name='login.html'), name='login'),
 path('profile/', views.profile, name='profile'),
 path('users/', views.user_list, name='user_list'),
 path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
]

