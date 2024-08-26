from django.urls import path,register_converter
from enroll.views import show_detail,show_years,show_details,show_subdetails,home_page
from enroll.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter,'yyyy')
urlpatterns = [
    path('stud/<int:my_id>', show_detail, name='detail'),   
    path('stud/<my_id>', show_details, name='details'),
    path('stud/<int:my_id>/<int:sub_id>', show_subdetails, name='subdetail'),   
    path('', home_page, name = 'home'),
    path('session/<yyyy:years>', show_years, name = 'years'),
    
]
