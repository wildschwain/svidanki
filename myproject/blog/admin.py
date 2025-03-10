from django.contrib import admin
from .models import Sity, Profile, Gender, The_purpose_of_dating

@admin.register(Sity)
class SityAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sity',)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(The_purpose_of_dating)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('title',)