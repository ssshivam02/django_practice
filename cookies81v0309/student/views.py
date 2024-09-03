from django.shortcuts import render
from datetime import timedelta, datetime
# Create your views here.
def setcookie(request):
    response =render(request,'student/setcookie.html')
    response.set_cookie('name','shivam',max_age=60, expires = datetime.now() + timedelta(days=2))
    return response

def setsignedcookie(request):
    response =render(request,'student/setcookie.html')
    response.set_signed_cookie('name','shivam',salt="nms" ,max_age=60, expires = datetime.now() + timedelta(days=2))
    return response

def getcookie(request):
    name = request.COOKIES.get('name')
    SCHOOL = request.COOKIES.get('School','D.A.V.')
    print(name)
    return render(request,'student/getcookie.html',{'nm':name,'school':SCHOOL})

def getsignedcookie(request):
    name = request.get_signed_cookie('name',salt='nm', default = "guest")
    return render(request,'student/getcookie.html',{'nm':name})

def deletecookie(request):
    response = render(request,'student/delcookie.html')
    response.delete_cookie("name")
    return response