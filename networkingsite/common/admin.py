from django.contrib import admin

# Register your models here.
class BaseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uuid",
        "__str__"
    )
    
    readonly_fields = [
        "uuid",
        "created_at",
        "modified_at"
    ]
