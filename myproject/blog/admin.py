from django.contrib import admin
from .models import Task, Sity, Profile, Gender, Age, The_purpose_of_dating

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')

@admin.register(Sity)
class SityAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sity',)

@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Age)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(The_purpose_of_dating)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('title',)