from django.urls import path
from course.views import course_info

urlpatterns = [
    path('django/', course_info, name= "course_django")
]