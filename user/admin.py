from django.contrib import admin
from user.models import User, UserTag


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'firstName', 'lastName', 'phone', 'password')


@admin.register(UserTag)
class UserTagAdmin(admin.ModelAdmin):
    list_display = ('tag', 'user', 'expiry')
