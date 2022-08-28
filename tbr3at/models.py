from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import timedelta

# Create your models here.
class User(AbstractUser):
  #Boolean fields to select the type of account.
  isUser = models.BooleanField(default=False)
  isCharity = models.BooleanField(default=False)

class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name

class Item(models.Model):
    condition_choices = [
        ("New", "New"),
        ("Like New", "Like New"),
        ("Used", "Used"),
    ]
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    condition = models.CharField(choices=condition_choices, max_length=15)
    isReserved = models.BooleanField(default=False)
    category_name = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="items",
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="items"
    )

    def __str__(self):
        return self.name
class Charity(models.Model):
    charity = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    phone = models.CharField(max_length=8)
    location = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Annoucement(models.Model):
    priority_choices = [
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    condition_choices = [
        ("New", "New"),
        ("Like New", "Like New"),
        ("Used", "Used"),
        ("any","any"),
    ]


    name = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    priority = models.CharField(choices=priority_choices, max_length=15)
    charity_name = models.ForeignKey(
        Charity,
        on_delete=models.CASCADE,
        related_name="annoucement",
    )
    quantity = models.PositiveIntegerField(default=0)
    duration = models.DurationField(default= timedelta(days=1), null=True)
    category_name = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="annoucement",
    )
    condition = models.CharField(choices=condition_choices, max_length=15)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=8 )
    image = models.ImageField(upload_to='images/', default="https://pngimage.net/wp-content/uploads/2018/06/profile-avatar-png-6.png", null=True, blank= True)
    location = models.TextField(max_length=250, null=True, blank=True)
    def __str__(self):
        return self.user.username