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
    # User CRUD
    path("users-all/", views.UsersListAPIView.as_view(), ),
    path("users-profile/", views.NormalUsersProfileListAPIView.as_view(), ),
    path("users-charity/", views.CharitiesProfileListAPIView.as_view(), ),
    path("users-profile/<int:object_id>/", views.UserProfileAPIView.as_view(), ),
    path("users-charity/<int:object_id>/", views.UserProfileAPIView.as_view(), ),
    path("users/<int:object_id>/update/", views.ProfileUpdateView.as_view(), name="update-profile"),
    path("users/points/<int:object_id>/", views.UpdsteUserPointsView.as_view(), name="update-points"),

    #Login and Registration path
    path("register-user/", views.UserRegistrationView.as_view(), name="register-user"),
    path("register-charity/", views.CharityRegistrationView.as_view(), name="register-charity"),
    path("login/", views.MyTokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),

    #Category CRUD
    path("category/", views.CategoriesListAPIView.as_view(), name="categories"),
    path("category/<int:object_id>/", views.OneCategoryAPIView.as_view(), name="category"),
    path("category/create/", views.CategoryCreateView.as_view(), name="category-create"),
    path("category/update/<int:object_id>/", views.CategoryUpdateView.as_view(), name="category-update"),
    path("category/delete/<int:object_id>/", views.CategoryDeleteView.as_view(), name="category-delete"),


    #Item CRUD
    path("item/", views.ItemsListAPIView.as_view(), name="items"),
    path("item/<int:object_id>/", views.OneItemAPIView.as_view(), name="item"),
    path("item/create/", views.ItemCreateView.as_view(), name="item-create"),
    path("item/<int:object_id>/update/", views.ItemUpdateView.as_view(), name="item-update"),
    path("item/<int:object_id>/delete/", views.ItemDeleteView.as_view(), name="item-delete"),
    path("item/<int:object_id>/reserve/", views.ReservedView.as_view(), name="item-reserve"),

    #Announcement CRUD
    path("announcement/", views.AnnoucementsListAPIView.as_view(), name="announcements"),
    path("announcement/<int:object_id>/", views.OneAnnoucementAPIView.as_view(), name="announcement"),
    path("announcement/create/", views.AnnouncementCreateView.as_view(), name="announcement-create"),
    path("announcement/update/<int:object_id>/", views.AnnoucementUpdateView.as_view(), name="announcement-update"),
    path("announcement/delete/<int:object_id>/", views.AnnoucementDeleteView.as_view(), name="announcement-delete"),
    path("announcement/donate/<int:object_id>/", views.DonateView.as_view(), name="donate"),


    #Report CRUD
    path("report/", views.ReportListAPIView.as_view(), name="reports"),
    path("report/<int:object_id>/", views.OneReportListAPIView.as_view(), name="report"),
    path("report/create/", views.ReportCreateView.as_view(), name="report-create"),

    # web paths
    path("home/",views.get_charity,name="home"),
    path("register-user/",views.register_user,name="register-user"),
    path("login-user/",views.login_user,name="login-user"),
    path("logout-user/",views.logout_user,name="logout-user"),
    path("create/category/", views.create_category, name="create-category"),
    path("create/item/", views.create_item, name="create-item"),
    path("category/<int:CategoryID>/", views.category_detail, name="category-detail"),
    path("item/<int:ItemID>/", views.item_detail, name="item-detail"),
    path("users/",views.get_User,name="users_list"),
    path("user-details/<int:user_id>/",views.get_user_details,name="user_details"),
    path("admin-update/<int:user_id>/",views.edit_admin_profile,name="admin-update"),

    



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
