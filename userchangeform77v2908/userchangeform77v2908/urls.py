"""userchangeform77v2908 URL Configuration

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
from enroll.views import change_password,sign_up,user_login,user_profile,user_logout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', sign_up, name='signup'),
    path('login/', user_login, name='login'),
    path('profile/', user_profile, name='profile'),
    path('logout/',user_logout, name = 'logout'),
    path('changepassword/', change_password, name="changepass"),
]