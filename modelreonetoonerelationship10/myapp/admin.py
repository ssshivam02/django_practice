from django.contrib import admin
from myapp.models import Page, User
# Register your models here.

# User model is already registed, so need to register again.
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=['page_name','page_cat','page_publish_date', 'user']

