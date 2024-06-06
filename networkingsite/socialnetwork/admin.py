from django.contrib import admin
from .models import User
from common.admin import BaseAdmin

# Register your models here.
class RegisteredUserAdmin(BaseAdmin):
    list_display = ["id", "uuid", "email", "first_name"]
    list_filter = ["id", "email"]
    search_fields = ["id", "uuid", "email", "first_name"]


admin.site.register(User, RegisteredUserAdmin)

