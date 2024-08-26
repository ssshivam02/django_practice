from django.shortcuts import render
from enroll.forms import StudentRegistration
from django.contrib import messages
# Create your views here.
def registration(request):
    if request.method=='POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save() 
            # messages.add_message(request, messages.SUCCESS,'Your form Successfully submitted.')
            # messages.add_message(request, messages.INFO,'Your form submitted.')   
            # shortcut message
            current_level=messages.get_level(request)
            messages.set_level(request,messages.DEBUG)
            # after set we need to pass.
            messages.debug(request,'This is debug')
            print(current_level)
            messages.success(request, "Your form Successfully submitted.")
            current_level=messages.get_level(request)
            print(current_level)
            messages.info(request, "Now you can login")
            messages.success(request, 'Update is done')
            messages.warning(request, 'Your form submitted.')
            messages.error(request, 'This is error')
    else:
        fm = StudentRegistration()        
    return render(request,'enroll/userregistration.html',{'form':fm})