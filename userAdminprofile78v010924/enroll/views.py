from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import SignUpForm,EditUserProfileForm,EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth  import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.models import User

# Signup view function.
def sign_up(request):
    if  request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account created successfully!!!')
            form.save()
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
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


# Profile
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser:
                fm = EditAdminProfileForm(request.POST, instance = request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance = request.user)
                users = None
            if fm.is_valid():
                messages.success(request, 'Profile Updated!!!')
                fm.save()
        else:
            if  request.user.is_superuser:
                fm= EditAdminProfileForm(instance= request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(instance= request.user)
                users = None
        return render(request, 'enroll/profile.html',{'name':request.user, 'form':fm, 'users':users})
    else:
        return HttpResponseRedirect('/login/')

# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

#Change password with old password.
def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # this will help in maintaining session.
                update_session_auth_hash(request,form.user)
                messages.success(request,'Passwrord Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            form= PasswordChangeForm(user=request.user)
        return render(request,'enroll/changepass.html',{'form':form})   
    else:
        return HttpResponseRedirect('/login/')
    
def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm = EditUserProfileForm(instance = pi)
        return render(request, 'enroll/userdetail.html',{"form":fm})
    else:
        return HttpResponseRedirect('/login')