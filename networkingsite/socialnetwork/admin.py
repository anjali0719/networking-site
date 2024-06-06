from django.contrib import admin
from .models import User, FriendRequest
from common.admin import BaseAdmin

# Register your models here.
class RegisteredUserAdmin(BaseAdmin):
    list_display = ["id", "uuid", "email", "first_name"]
    list_filter = ["id", "email"]
    search_fields = ["id", "uuid", "email", "first_name"]

class FriendRequestAdmin(BaseAdmin):
    list_display = ["uuid", "from_user", "to_user", "status"]
    list_filter = ["uuid", "from_user", "to_user", "status"]
    search_fields = ["uuid", "from_user", "to_user", "status"]

admin.site.register(User, RegisteredUserAdmin)
admin.site.register(FriendRequest, FriendRequestAdmin)
