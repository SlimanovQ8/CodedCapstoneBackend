from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from .models import Charity, Category, Annoucement, UserProfile, Item
from .serializers import UsersListSerializer, UsersProfileListSerializer, UpdateProfileSerializer, UserCreateSerializer, CustomTokenObtainPairSerializer, GetUserProfile
from .permissions import IsOwner

# Create your views here.

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer

class UsersProfileListAPIView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UsersProfileListSerializer

class UserProfileAPIView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class =  GetUserProfile
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class ProfileUpdateView(UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UpdateProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsOwner]
