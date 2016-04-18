from django.contrib import admin
from models import UserMessage
# Register your models here.
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('owner','content','status','create_timestamp','last_update_timestamp')
    search_fields = ('content',)
    list_filter = ('status',)

admin.site.register(UserMessage,UserMessageAdmin)