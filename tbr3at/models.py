import datetime

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class User(AbstractUser):
  #Boolean fields to select the type of account.
  username = models.CharField(max_length=40, blank=True, null=True, unique=True)
  charityname = models.CharField(max_length=40, blank=True, null=True)
  name = models.CharField(max_length=40, blank=True, null=True)
  description = models.TextField(blank=True, null=True)
  image = models.ImageField(upload_to='images/', blank=True, null=True)
  rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], blank=True, null=True, default=0.0)
  phone = models.CharField(max_length=8, blank=True, null=True)
  location = models.CharField(max_length=250, blank=True, null=True)
  isUser = models.BooleanField(default=False)
  isCharity = models.BooleanField(default=False)
  numOfDonation = models.PositiveIntegerField(default=0)
  points = models.PositiveIntegerField(default=0)

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
    condition = models.CharField(choices=condition_choices, max_length=15, null=True, blank=True)
    isReserved = models.BooleanField(default=False)
    isApproved = models.BooleanField(default=False)
    category_name = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="items",
        null=True,
        blank=True,
    )
    charity_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="by",
        null=True,
        blank=True,
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
    description = models.TextField(null= True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0.0)
    phone = models.CharField(max_length=8, null=True, blank=True)
    location = models.CharField(max_length=250, null=True, blank=True)
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
        User,
        on_delete=models.CASCADE,
        related_name="annoucement",
    )
    quantity = models.PositiveIntegerField(default=0)
    remaining = models.PositiveIntegerField(default=0)
    duration = models.DateField()
    category_name = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="annoucement",
    )
    condition = models.CharField(choices=condition_choices, max_length=15)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=8, null=True, blank=True)
    image = models.ImageField(upload_to='images/', default="https://pngimage.net/wp-content/uploads/2018/06/profile-avatar-png-6.png", null=True, blank= True)
    location = models.TextField(max_length=250, null=True, blank=True)
    numOfDonation = models.PositiveIntegerField(default=0)
    points = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.user.username

class Report(models.Model):
    title = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField()
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reportCreator",

    )
    to = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="reportedTo",

    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        related_name="item",

    )
