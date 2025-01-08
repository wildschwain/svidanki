from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

#------------------------------------------------------------ Профиль - Редактирование Профиля

class Sity(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Gender(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Age(models.Model):
    title = models.PositiveIntegerField()

    def __str__(self):
        return str(self.title)

class The_purpose_of_dating(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    age = models.ForeignKey(Age, on_delete=models.CASCADE, blank=True, null=True, related_name='year')
    sity = models.ForeignKey(Sity, on_delete=models.CASCADE, blank=True, null=True, related_name='residents')
    about_me = models.TextField(blank=True, null=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, blank=True, null=True, related_name='gena')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    the_purpose_of_dating = models.ForeignKey(The_purpose_of_dating, on_delete=models.CASCADE, blank=True, null=True, related_name='zel')
    preferences = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
    
#------------------------------------------------------------ Поиск пользователя