from django.contrib import admin
from models import UserProfile

# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('owner','avatar','create_timestamp','last_update_timestamp')

admin.site.register(UserProfile,UserProfileAdmin)