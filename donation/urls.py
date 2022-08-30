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
    path("users-all/", views.UsersListAPIView.as_view(), ),
    path("users-profile/", views.NormalUsersProfileListAPIView.as_view(), ),
    path("users-charity/", views.CharitiesProfileListAPIView.as_view(), ),
    path("users-profile/<int:object_id>/", views.UserProfileAPIView.as_view(), ),
    path("users-charity/<int:object_id>/", views.UserProfileAPIView.as_view(), ),
    path("users/<int:object_id>/update/", views.ProfileUpdateView.as_view(), name="update-profile"),
    path("register-user/", views.UserRegistrationView.as_view(), name="register-user"),
    path("register-charity/", views.CharityRegistrationView.as_view(), name="register-charity"),
    path("login/", views.MyTokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    
    
    
    
    
    
    
    # web paths
    path("home/",views.home_Page,name="home"),
    path("register-user/",views.register_user,name="register-user"),
    path("login-user/",views.login_user,name="login-user"),
    path("logout-user/",views.logout_user,name="logout-user"),
    path("create/category/", views.create_category, name="create-category"),
    path("create/item/", views.create_item, name="create-item"),
    path("category/<int:CategoryID>/", views.category_detail, name="category-detail"),
    path("item/<int:ItemID>/", views.item_detail, name="item-detail"),
    path("users/",views.get_User,name="users_list"),
    path("user-details/<int:user_id>/",views.get_user_details,name="user_details"),

    



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
