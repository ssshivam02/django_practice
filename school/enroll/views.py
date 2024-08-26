from django.shortcuts import render
from enroll.models import Students
from django.http import HttpResponseRedirect
from enroll.forms import StudentRegistration
from enroll.models import User
# Create your views here.
def studentinfo(request):
    student=Students.objects.all()
    print(student)
    return render(request,'enroll/studentdetails.html',{'student':student})

def thankyou(request):
    return render(request,'enroll/success.html')

def showformdata(request):
    # intial is for showing pre defind value in form
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            # print('Name:',fm.cleaned_data['first_name'])
            # print('email:', fm.cleaned_data['email'])
            # print('password:', fm.cleaned_data['password'])
            nm = fm.cleaned_data['first_name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            # reg = User(name=nm,email=em,password=pw)
            # reg.save()
            reg = User(id=1) # it will delete data after clicking submit button.
            reg.delete()
            # redirect to other webpage
            # simple
            # return render(request, 'enroll/success.html',{'name':fm.cleaned_data['first_name']})
            # by usinh httpResponseRedirect
            return HttpResponseRedirect('/enroll/success/')
            
    else:
        fm = StudentRegistration()
        print('This is get')
        fm= StudentRegistration(label_suffix="-", initial={'first_name': 'shivam'})
        fm.order_fields(field_order=['email', 'first_name','name'])
    return render(request, 'enroll/userregistration.html',{'form':fm})