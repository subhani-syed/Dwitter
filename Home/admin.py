from django.contrib import admin
from .models import Profile,Dweet,UserFollowing
# Register your models here.

admin.site.register(Profile)
admin.site.register(Dweet)
admin.site.register(UserFollowing)