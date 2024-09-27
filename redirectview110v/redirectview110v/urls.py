"""redirectview110v URL Configuration

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
from school.views import TemplateView,ShivamRedirectView,RedirectView, ShivamSharmaRedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name ='school/home.html'), name = 'blankhome'),
    # redirectView
    path('home/', RedirectView.as_view(url='/'), name = 'hom'),
    # path('index/', RedirectView.as_view(url='/'), name = 'index'),
    # pattern of home
    path('index/', RedirectView.as_view(pattern_name = 'hom'), name = 'index'),
    
    
    path('shivamsharma/', RedirectView.as_view(url='https://www.google.com'), name='google'),
    
    path('shivamsharma1/', ShivamSharmaRedirectView.as_view(), name = 'shivaminviews'),
    
    # it will redirect it mindex
    path('shivam/<int:pk>/', ShivamRedirectView.as_view(), name ='shivam'),
    path('roll/<int:pk>/', TemplateView.as_view(template_name='school/home.html'), name ='mindex'),
    # path('home/<slug:post>', ShivamRedirectView.as_view(), name ='shivam'),
    # path('<slug:post>/', TemplateView.as_view(template_name ='school/home.html'), name ='mindex')
    
    
    # query string
    path('query/', ShivamRedirectView.as_view(url='/home/?query=django', permanent = False
                                        ), name = 'query'),
]
