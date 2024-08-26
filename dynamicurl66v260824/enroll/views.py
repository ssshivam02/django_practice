from django.shortcuts import render

# Create your views here.
def show_details(request, my_id):
    return render(request, 'enroll/show.html',{'id':my_id,})

def show_subdetails(request, my_id,sub_id):
    return render(request, 'enroll/show.html',{'id':my_id,'sub_id':sub_id})

def home_page(request):
    return render(request, 'enroll/home.html')
def show_years(request, years):
    return render(request, 'enroll/years.html',{'yyyy':years})

# my_id=1 is default .
def show_detail(request, my_id=1):
    if my_id == 1:
        student = {'id':my_id, 'name' : 'shivam'}
    return render(request, 'enroll/show.html',student)