
from django.urls import path
from fees.views import fees_django, fees_python

urlpatterns = [
    path('feedj/', fees_django),
    path('feepy/', fees_python)
]