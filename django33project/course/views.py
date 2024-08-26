from django.shortcuts import render

# Create your views here.
def course_info(request):
    return render(request, 'course/courseinfo.html')
