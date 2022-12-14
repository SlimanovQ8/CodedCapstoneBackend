
from rest_framework import generics
from rest_framework.generics import ListAPIView, DestroyAPIView, UpdateAPIView, CreateAPIView, RetrieveAPIView
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from .models import Charity, Category, Annoucement, UserProfile, Item, User, Report
from tbr3at import  serializers
from .permissions import IsOwner
from tbr3at import models
from .forms import RegisterForm,LoginForm,CategoryForm,itemForm,AdminForm
from django.contrib.auth import login,authenticate,logout
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from django.db.models import Count, Avg, Sum


# Create your views here.


class UserRegistrationView(CreateAPIView):
    serializer_class = serializers.UserCreateSerializer

class CharityRegistrationView(CreateAPIView):
    serializer_class = serializers.CharityCreateSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializers.CustomTokenObtainPairSerializer

class UsersListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.GetAllUsersSerializers

class NormalUsersProfileListAPIView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.GetAllNormalUsersSerializers

class UserProfileAPIView(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.GetAllNormalUsersSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class CharityProfileAPIView(RetrieveAPIView):
    queryset = Charity.objects.all()
    serializer_class = serializers.GetAllCharitySerialzers
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class ProfileUpdateView(UpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UpdateProfileSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsOwner]


class CharitiesProfileListAPIView(ListAPIView):
    queryset = Charity.objects.all()
    serializer_class = serializers.GetAllCharitySerialzers


class AnnoucementsListAPIView(ListAPIView):
    queryset = Annoucement.objects.all()
    serializer_class = serializers.GetAllAnnoucementSerializers



class CategoriesListAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.GetAllCategoriesSerializers

class ItemsListAPIView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.GetAllItemsSerializers
#
class OneAnnoucementAPIView(RetrieveAPIView):
    queryset = Annoucement.objects.all()
    serializer_class = serializers.GetAllAnnoucementSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class OneCategoryAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.GetAllCategoriesSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class OneItemAPIView(RetrieveAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.GetAllItemsSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'



class ItemCreateView(CreateAPIView):
    serializer_class = serializers.ItemCreateSerializer


class ReportCreateView(CreateAPIView):
    serializer_class = serializers.ReportCreateSerializer


class ReportListAPIView(ListAPIView):
    queryset = Report.objects.all()
    serializer_class = serializers.GetAllReportsSerializers


class OneReportListAPIView(ListAPIView):
    queryset = Report.objects.all()
    serializer_class = serializers.GetAllReportsSerializers
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class CategoryCreateView(CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AnnouncementCreateView(CreateAPIView):
    serializer_class = serializers.AnnoucementCreateSerializer



class ItemUpdateView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsAuthenticated, IsOwner]


class CategoryUpdateView(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsAuthenticated, IsOwner]


class AnnoucementUpdateView(UpdateAPIView):
    queryset = Annoucement.objects.all()
    serializer_class = serializers.AnnoucementUpdateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class DonateView(UpdateAPIView):
    queryset = Annoucement.objects.all()
    serializer_class = serializers.DonateSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

class ReservedView(UpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = serializers.ItemUpdateReserved
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'


class UpdsteUserPointsView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.updateUserPointsSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'

"""delete item view"""


class ItemDeleteView(DestroyAPIView):
    queryset = Item.objects.all()
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsOwner]


"""delete category view"""


class CategoryDeleteView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategoryDeleteSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsAuthenticated, IsOwner]


"""delete annoucement view"""


class AnnoucementDeleteView(DestroyAPIView):
    queryset = Annoucement.objects.all()
    serializer_class = serializers.AnnoucementDeleteSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'object_id'
    permission_classes = [IsAuthenticated, IsOwner]


##############################################################################################
#  WEB VIWES 
#############################################################################################

# View for home page 
def home_Page(request):
    categories: list[models.Category] = list(models.Category.objects.all())

    context = {
        "categories": categories,
    }
    return render(request,"home_page.html",context)


def register_user(request):
    form =  RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(user.password)
            print(user.first_name)
            user.save()
            print(user)

            login(request,user)
            return redirect("home")
    context = {
        "form":form,
    }
    return render (request, "register.html",context)



# Login View 
def login_user(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            print(username)
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            return redirect("home")
        
    context = {
        "form": form,
    }
    return render(request, "login.html", context)





#logout view 
def logout_user(request):
    logout(request)
    return redirect("home")



#create ctegory
def create_category(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("login")

    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            categor = form.save(commit=False)
            categor.created_by = request.user
            categor.save()
            return redirect("home")

    context = {
        "form": form,
    }

    return render(request, "create_category.html", context)





 # create Item
def create_item(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("login")
    
    form = itemForm()
    if request.method == "POST":

        form = itemForm(request.POST, request.FILES)

        if form.is_valid():
            rec = form.save(commit=False)
            rec.created_by = request.user
            rec.save()
            form.save_m2m()
            return redirect("home")

    context = {
        "form": form,
    }

    return render(request, "create_item.html", context)





#category details
def category_detail(request, CategoryID):
    category = models.Category.objects.get(id=CategoryID)
    context = {
        "categories": {
            "name": category.name,
            "description": category.description,
            "image": category.image,
        }

    }

    return render(request, "category_detail.html", context)


# item details

def item_detail(request, ItemID):
    Rec = models.Item.objects.get(id=ItemID)

    context = {
        "item": {
            "name": Rec.name,
            "description": Rec.description,
            "image": Rec.image,
            "condition": Rec.condition,
            "isReserved": Rec.isReserved,
            "category_name": Rec.category_name,
            "created_by":Rec.created_by

        }
      

    }

    return render(request, "item_detail.html", context)




# User Lists 
def get_User(request):
    users = User.objects.all()
    context = {"users":users}
    return render(request,"home_page.html",context)

def getReports(request):
    reports = Report.objects.all()
    context = {"report":reports}
    return render(request,"notification.html",context)
#User details
def get_user_details(request,user_id):
    user=User.objects.get(id=user_id)

    context= {
        "user": {
            "name": user.name,
            "username": user.username,
            "rating": user.rating,
            "phone": user.phone,
            "location": user.location,
            "image": user.image,
    
        }
       
    }
    return render (request,"user-details.html",context)


# Charity Lists 
def get_charity(request):
    users = User.objects.filter(isUser=True).all()
    allUsers = User.objects.all()
    items = Item.objects.all()
    totalDonation = list(User.objects.all().aggregate(Sum('numOfDonation')).values())[0]

    charites = User.objects.filter(isCharity=True).all()
    context = {
        "users":users,
        "charities": charites,
        "allUsers": allUsers,
        "items": items,
        "totalDonation": totalDonation

               }
    return render(request,"dashboard.html",context)



#Admin Update
def edit_admin_profile(request: HttpRequest, user_id) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect("login")
    obj = models.User.objects.get(id= user_id)
    form = AdminForm()
    if request.method == "POST":

        form = AdminForm(request.POST, request.FILES, instance=obj)

        if form.is_valid():
            rec = form.save(commit=False)
            rec.created_by = request.user
            rec.save()
            return redirect("dashboard.html")

    context = {
        "obj": obj,
        "form": form,

    }
    return render(request,"admin-setting.html",context)



