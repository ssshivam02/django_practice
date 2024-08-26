from django.contrib import admin
from enroll.models import Students, User
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('stuid','stuname','stuemail','stupass','comment')

admin.site.register(Students, StudentAdmin)

@admin.register(User)
class UserAdmi(admin.ModelAdmin):
    list_display = ('id','name','email','password')
