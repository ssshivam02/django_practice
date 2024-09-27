from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    ip = request.session.get('ip',0)
    print(ip)
    return HttpResponse("Hello World")