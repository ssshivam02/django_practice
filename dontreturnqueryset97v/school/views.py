from django.shortcuts import render
from school.models import Student

# Create your views here
# get().
def home(request):
    # student_data = Student.objects.get(id=1) #pk is primary key == id
    # student_data = Student.objects.first()
    # student_data = Student.objects.last()
    #create
    # student_data, created = Student.objects.get_or_create(name='sameer',roll ='3', address='bihar', marks=100,pass_date='2020-05-01')
    # student_data= Student.objects.filter(id=3).update(name='king',marks=820) # update query only work with filter
    # student_data, created = Student.objects.update_or_create(name='king', roll=3, defaults={'name':'John'})
    # print("Return data:", student_data)
    # print('Created:', created)
    
    
    # bluk_update
    all_student_data = Student.objects.all()
    for stu in all_student_data:
        stu.address = 'Bhel'
    student_data = Student.objects.bulk_update(all_student_data,['address'])
    return render(request, 'school/home.html',{'student':student_data})

