from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your models here.
# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True)

#     def __str__(self):
#         return self.username

# class CustomUSerAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = CustomUser
#     list_display = ['email', 'username']

class Book(models.Model):
    title = models.CharField(max_length=64)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
