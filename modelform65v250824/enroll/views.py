from django.shortcuts import render
from enroll.models import Students
from django.http import HttpResponseRedirect
from enroll.forms import StudenRegistrationModelForm
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
        # for update, pk == id
        pi= User.objects.get(pk=2)
        fm = StudenRegistrationModelForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            # print('Name:',fm.cleaned_data['name'])
            # print('email:', fm.cleaned_data['email'])
            # print('password:', fm.cleaned_data['password'])
            # password= fm.cleaned_data['password']
            # email= fm.cleaned_data['email']
            # Name= fm.cleaned_data['name']
            #reg = User(name=Name, email=email, password= password)
            #FOR UPDATE
            # reg = User(id=1,name=Name, email=email, password= password)
            # reg.save()
            #for delete
            # reg = User(id=1)
            # reg.delete()
            return HttpResponseRedirect('/enroll/success/')       
    else:
        fm = StudenRegistrationModelForm()
        print('This is get')
        fm= StudenRegistrationModelForm(label_suffix="-")
        fm.order_fields(field_order=['email', 'name','password'])
    return render(request, 'enroll/userregistration.html',{'form':fm})