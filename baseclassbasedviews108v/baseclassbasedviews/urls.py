"""baseclassbasedviews URL Configuration

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
from school.views import NewsClassViewParameter, myview,newsfun, newsfun_parameter,contactfun, homefun, NewsClassView, ContantClassView,MyView, HomeClassView, MyViewChild
urlpatterns = [
    path('admin/', admin.site.urls),
    path('func/', myview, name = "func"),
    path('homefun/', homefun, name="homefun"),
    path('newsfun/', newsfun, name = 'newsfun'),
    path('newsfun_p/', newsfun_parameter,{'template_name':'school/news.html'}, name ="newsfun_p"),
    path('newsfun_p2/', newsfun_parameter,{'template_name':'school/news1.html'}, name ="newsfun_p2"),
    path('contactfun/', contactfun, name='contactfun'),
    # path('cl/', MyView.as_view(), name ='cl')
    # here we passing name dynamically
    path('cl/', MyView.as_view(name="shivam"), name='cl'),
    path('subcl/', MyViewChild.as_view(), name ='subcl'),
    path('homecl/', HomeClassView.as_view(), name='homecl'),
    path('contactcl/', ContantClassView.as_view(), name='contactcl'),
    path('newscl/', NewsClassView.as_view(), name ="newscl" ),
    path('newsclp/',NewsClassViewParameter.as_view(), {'template_name':'school/news.html'}, name ="newsfun_p"),
    path('newsclp1/',NewsClassViewParameter.as_view(), {'template_name':'school/news1.html'}, name ="newsfun_p2")
]
