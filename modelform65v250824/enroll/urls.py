from django.urls import path
from enroll.views import studentinfo, showformdata, thankyou

urlpatterns = [
    path('stud/', studentinfo),
    path('form/', showformdata),
    path('success/',thankyou)
]
