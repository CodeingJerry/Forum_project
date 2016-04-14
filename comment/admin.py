from django.contrib import admin
from models import Comment

# Register your models here.
class CommentAdmin(admin.ModelAdmin):
    list_display=("block","article","content","owner","status","create_timestamp","last_update_timestamp")
    list_filter = ('block',)
    search_fields = ['article','content',]

admin.site.register(Comment,CommentAdmin)