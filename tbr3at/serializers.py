from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainSerializer, TokenObtainPairSerializer

from .models import UserProfile, Charity, Category, Annoucement, Item, User, Report
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
        token['id'] = user.id
        token["isCharity"] = user.isCharity
        token["isUser"] = user.isUser
        token["name"] = user.name
        token["chatrityName"] = user.charityname
        token["location"] = user.location
        token["phone"] = user.phone
        token["rating"] = user.rating
        token["description"] = user.description
        token["points"] = user.points
        token["numOfDonation"] = user.numOfDonation

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


class GetAllCategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class GetAllAnnoucementSerializers(serializers.ModelSerializer):
    charity_name = GetAllUsersSerializers()
    category_name = GetAllCategoriesSerializers()

    class Meta:

        model = Annoucement
        fields = "__all__"

class GetAllItemsSerializers(serializers.ModelSerializer):
    created_by = GetAllUsersSerializers()
    category_name = GetAllCategoriesSerializers()
    charity_name = GetAllUsersSerializers()
    class Meta:
        model = Item
        fields = "__all__"


class GetAllReportsSerializers(serializers.ModelSerializer):
    created_by = GetAllUsersSerializers()
    to = GetAllUsersSerializers()
    class Meta:
        model = Report
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
        fields = ["name", "email", "username", "password", "phone", "location", "image"]

    def create(self, validated_data):
        name = validated_data["name"]
        email = validated_data["email"]
        username = validated_data["username"]
        password = validated_data["password"]
        phone = validated_data["phone"]
        image = validated_data["image"]
        location = validated_data["location"]


        new_user = User(name=name, email= email, username= username, phone=phone, isUser=True, location=location, image=image)
        new_user.set_password(password)
        new_user.save()
        newProfile = UserProfile(user=new_user, id= new_user.id, phone=phone, location=location, image=image)
        newProfile.save()

        return validated_data


class CharityCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["charityname", "email" , "password", "phone", "location", "image"]

    def create(self, validated_data):
        name = validated_data["charityname"]
        email = validated_data["email"]
        username = validated_data["charityname"]
        password = validated_data["password"]
        phone = validated_data["phone"]
        image = validated_data["image"]
        location = validated_data["location"]
        # description = validated_data["description"]


        new_user = User(name=name, charityname= username,  email= email, username= name, phone=phone, isCharity=True, location=location, image=image)
        new_user.set_password(password)
        new_user.save()
        newCharity = Charity(charity=new_user, id= new_user.id, name=name, phone=phone, location=location, image=image)
        newCharity.save()

        return validated_data

class ItemCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ["name", "description", "image", "condition", "category_name"]
        extra_kwargs = {
            "owner": {
                "read_only": True
            }
        }

    def create(self, validated_data):
        name = validated_data["name"]
        description = validated_data["description"]
        image = validated_data["image"]
        condition = validated_data["condition"]
        category_name = validated_data["category_name"]
        owner = self.context["request"].user

        newItem = Item(name=name, description=description, image=image, condition=condition, category_name=category_name, created_by=owner)
        newItem.save()

        return validated_data

class ReportCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Report
        fields = ["title", "description", "to", "item"]
        extra_kwargs = {
            "owner": {
                "read_only": True
            }
        }

    def create(self, validated_data):
        title = validated_data["title"]
        description = validated_data["description"]
        to = validated_data["to"]
        item = validated_data["item"]
        owner = self.context["request"].user

        newReport = Report(title=title, description=description, created_by=owner, to=to, item=item)
        newReport.save()

        return validated_data

class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name", "description", "image"]

    def create(self, validated_data):
        name = validated_data["name"]
        description = validated_data["description"]
        image = validated_data["image"]

        newCategory = Category(name=name, description=description, image=image)
        newCategory.save()

        return validated_data

class AnnoucementCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Annoucement
        fields = ["name", "description", "image", "category_name", "priority", "duration", "quantity"]
        extra_kwargs = {
            "owner": {
                "read_only": True
            }
        }
    def create(self, validated_data):
        name = validated_data["name"]
        description = validated_data["description"]
        image = validated_data["image"]
        category = validated_data["category_name"]
        priority = validated_data["priority"]
        duration = validated_data["duration"]
        quantity = validated_data["quantity"]
        owner = self.context["request"].user
        newAnnoucement = Annoucement(name=name, description=description, image=image, category_name=category, priority=priority, condition="New", charity_name=owner, duration=duration, quantity=quantity, remaining=quantity)
        newAnnoucement.save()

        return validated_data

"""item update serializer"""
class ItemUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ["name", "description", "image", "category"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

"""category update serializer"""
class CategoryUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name", "description", "image"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

"""annoucement update serializer"""
class AnnoucementUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Annoucement
        fields = ["name", "description", "image", "category"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

class DonateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Annoucement
        fields = ["remaining"]

class ItemUpdateReserved(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ["isReserved", "charity_name"]

class updateUserPointsSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["points", "numOfDonation"]


"""item delete serializer"""
class ItemDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ["name", "description", "image", "category"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance

"""category delete serializer"""
class CategoryDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["name", "description", "image"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.save()
        return instance

"""annoucement delete serializer"""
class AnnoucementDeleteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Annoucement
        fields = ["name", "description", "image", "category"]

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.image = validated_data.get('image', instance.image)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance


