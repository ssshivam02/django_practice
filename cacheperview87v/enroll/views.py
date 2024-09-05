from django.shortcuts import render
from django.views.decorators.cache import cache_page
# Create your views here.
# views cache
@cache_page(30)
def home(request):
    return render(request, 'enroll/course.html')

def contact(request):
    return render(request, 'enroll/contact.html')