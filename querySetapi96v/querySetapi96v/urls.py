"""querySetapi96v URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from school.views import using_alias,values_list,values,reverse_student,order_by_student,all_student, one_student, exclude_student

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_student),
    path('one/', one_student),
    path('exclude', exclude_student),
    path('order_by_student/', order_by_student),
    path('reverse', reverse_student),
    path('values/', values),
    path('values_list/',values_list),
    path('using_alias/',using_alias)
]
