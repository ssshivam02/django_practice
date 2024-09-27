from django.shortcuts import render,HttpResponse
from django.template.response import TemplateResponse

# Create your views here.
def excp(request):
    print("I am Excp view")
    a = 10/0
    return HttpResponse("This is Exception page.")

def user_info(request):
    print("I am user_info view")
    user = {"name": "John"}
    return TemplateResponse(request,"hookmiddleware/user.html", user)
