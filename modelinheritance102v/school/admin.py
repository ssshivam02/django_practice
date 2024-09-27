from django.contrib import admin
from school.models import ExamCenter, MyExamCenterProxy ,Parent, Child,Student, Teacher, Contractor

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','name','age','roll_no','fees')
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display=('id', 'name','age','salary','date','subject')
    
@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','payment','date')
        
@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = ('id','city','pname')

@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('id','city','pname', 'roll','sname')
    
@admin.register(ExamCenter)
class ExamCenterAdmin(admin.ModelAdmin):
    list_display = ('id','cname','city')

@admin.register(MyExamCenterProxy)
class MyExamCenterProxyAdmin(admin.ModelAdmin):
    list_display = ('id','cname','city')