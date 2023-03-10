"""my_django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from hello.views import index
from hello.views import login_user
from hello.views import visitor
from hello.views import sign_in
from hello.views import sign_up

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/index', index),      ## if empty it will lead to the main page
    path('hello/login_user', login_user),
    path('hello/visitor', visitor),
    path('hello/sign_in', sign_in),
    path('hello/sign_up', sign_up),
]
