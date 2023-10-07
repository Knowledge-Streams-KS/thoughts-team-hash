from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=["id","username"]
    exclude=["content"]
    # fields =["name"]
    # readonly_fields = ["id","created_at"]
    search_fields=['username']



admin.site.register(User,UserAdmin)
