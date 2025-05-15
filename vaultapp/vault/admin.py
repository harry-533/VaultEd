from django.contrib import admin
from .models import CustomUser, Module
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('user_type',)}),
    )


admin.site.register(CustomUser)
admin.site.register(Module)