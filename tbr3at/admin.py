from django.contrib import admin

# Register your models here.
from .models import Category, Item, Charity, Annoucement, UserProfile, User

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Charity)
admin.site.register(Annoucement)
admin.site.register(UserProfile)
admin.site.register(User)