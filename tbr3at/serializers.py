from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenObtainPairSerializer

from .models import UserProfile, Charity, Category, Annoucement, Item, User

from rest_framework.authtoken.models import Token

from django.utils.translation import gettext_lazy as _
"""
    Register Normal User
"""

"""
    Sign in for both charity & custom user
"""
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user):
        token = super(CustomTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        token['first_name'] = user.first_name
        token['email'] = user.email
        token['user_id'] = user.id
        token["isCharity"] = user.isCharity
        token["name"] = user.name
        token["chatrityName"] = user.charityname
        token["location"] = user.location
        token["phone"] = user.phone
        token["rating"] = user.rating
        token["description"] = user.description

        return token

"""
    Get All users info (Charity or Normal users)
"""
class GetAllUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

"""
    Get Only Normal Users
"""
class GetAllNormalUsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

"""
    Get Only Charities
"""
class GetAllCharitySerialzers(serializers.ModelSerializer):
    class Meta:
        model = Charity
        fields = "__all__"


class UsersProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"

class UpdateProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['phone', 'image', "location"]

    def check_user(self, obj):
        if obj.owner != self.context["request"].user:
            raise serializers.ValidationError("You are not the owner of this profile")
        

# we might use this

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["name", "email", "username", "password", "phone", "image", "location"]

    def create(self, validated_data):
        name = validated_data["name"]
        email = validated_data["email"]
        username = validated_data["username"]
        password = validated_data["password"]
        phone = validated_data["phone"]
        image = validated_data["image"]
        location = validated_data["location"]


        new_user = User(name=name, email= email, username= username, phone=phone, image=image, isUser=True, location=location)
        new_user.set_password(password)
        new_user.save()
        newProfile = UserProfile(user=new_user, id= new_user.id, phone=phone, image=image, location=location)
        newProfile.save()

        return validated_data


class CharityCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["charityname", "email", "username", "password", "phone", "image", "location", "description"]

    def create(self, validated_data):
        name = validated_data["charityname"]
        email = validated_data["email"]
        username = validated_data["username"]
        password = validated_data["password"]
        phone = validated_data["phone"]
        image = validated_data["image"]
        location = validated_data["location"]
        description = validated_data["description"]


        new_user = User(name=name, charityname= username,  email= email, username= username, phone=phone, image=image, isCharity=True, location=location, description=description)
        new_user.set_password(password)
        new_user.save()
        newCharity = Charity(charity=new_user, id= new_user.id, name=name, description=description, phone=phone, image=image, location=location)
        newCharity.save()

        return validated_data