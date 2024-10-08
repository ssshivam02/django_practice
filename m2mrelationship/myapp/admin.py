from django.contrib import admin
from myapp.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['post_title', 'post_cat', 'post_publish_date', 'user']