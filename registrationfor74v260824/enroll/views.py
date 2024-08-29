from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from enroll.forms import SignUpForm
from django.contrib import messages
# Create your views here.
# def sign_up(request):
#     if  request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = UserCreationForm()
#     return render(request, 'enroll/signup.html',{'form':form})


def sign_up(request):
    if  request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request,'Account created successfully!!!')
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'enroll/signup.html',{'form':form})