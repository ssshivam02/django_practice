from django.contrib import admin
from enroll.models import User
# Register your models here.


@admin.register(User)
class UserAdmi(admin.ModelAdmin):
    list_display = ('id','name','email','password')
