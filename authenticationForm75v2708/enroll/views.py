from django.shortcuts import render,HttpResponseRedirect
from enroll.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import SetPasswordForm,AuthenticationForm,PasswordChangeForm
from django.contrib.auth  import authenticate, login, logout,update_session_auth_hash

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
        return render(request, 'enroll/profile.html',{'name':request.user})
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
    
#Change password without old password.
def change_without_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                # this will help in maintaining session.
                update_session_auth_hash(request,form.user)
                messages.success(request,'Passwrord Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            form= SetPasswordForm(user=request.user)
        return render(request,'enroll/changepass1.html',{'form':form})   
    else:
        return HttpResponseRedirect('/login/')
    
    