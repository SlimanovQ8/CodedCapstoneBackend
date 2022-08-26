"""donation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from tbr3at import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
path("users-list/", views.UsersListAPIView.as_view(), ),
    path("users-profile/", views.UsersProfileListAPIView.as_view(), ),
    path("users-profile/<int:object_id>/", views.UserProfileAPIView.as_view(), ),
    path("users/<int:object_id>/update/", views.ProfileUpdateView.as_view(), name="update-profile"),

    path("register/", views.UserCreateAPIView.as_view()),
    path("login/", views.MyTokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
]
