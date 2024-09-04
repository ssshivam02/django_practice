from django.shortcuts import render, HttpResponse
from datetime import timedelta, datetime
# Create your views here.
def setsession(request):
    request.session['name']='Shivam' 
    return render(request,'student/setsession.html')

def getsession1(request):
    if 'name' in request.session:
        name=request.session['name']
        request.session.modified=20 # 20 sec session will increase
        return render(request,'student/getsession1.html',{'name':name})
    else:
        return HttpResponse("Your session has expired...")

def getsession(request):
    # return_name = request.session['name']
    return_name= request.session.get('name',default="Suraj")
    print(return_name)
    keys = request.session.keys()
    age = request.session.setdefault('age','26')
    # items = request.session.items()  touple (keys, value)
    return render(request,'student/getsession.html',{'nm':return_name, 'keys':keys,'age':age})

def deletesession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'student/delsession.html')

def flushsession(request):
    request.session.flush()
    # cleared expired session from db
    # request.session.clear_expired()
    return render(request,'student/delsession.html')

def setsession1(request):
    request.session['name'] = 'prapti'
    # request.session.set_expiry(600) # 10 mins
    # request.session.set_expiry(0) # delete after browser close. 
    return render(request,'student/setsession1.html')

# def getsession1(request):
#     name = request.session['name']
#     return render(request,'student/getsession1.html', {'nm':name})

# test cookie
def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'student/settestcookie.html')

def checktestcookie(request):
    print(request.session.test_cookie_worked())
    return render(request, 'student/checktestcookie.html')

def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'student/deltestcookie.html')



