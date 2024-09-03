from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth  import authenticate, login, logout
from django.contrib.auth.models import Group
# Signup view function.
def sign_up(request):
    if  request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account created successfully!!!')
            user = form.save()
            group = Group.objects.get(name='editor')
            user.groups.add(group)
    else:
        form = SignUpForm()
    return render(request, 'enroll/signup.html',{'form':form})

# Login View function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request,data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data.get('username')
                password = fm.cleaned_data.get('password')
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/dashboard/')


# Dashboard
def user_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/dashboard.html', {'name':request.user.username})
    else:
        return HttpResponseRedirect('/login/')

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
