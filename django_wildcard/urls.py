"""django_wildcard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import calculator
from . import login
from . import prankpatrol
from . import command

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', prankpatrol.prankpatrol, name = 'home'),
    path('calculator/', calculator.calculate, name = 'calculate'),
    path('login/', login.login, name = 'login'),
    path('login_csrf/', login.login_csrf, name='login_csrf'),
    path('prankpatrol/', prankpatrol.prankpatrol, name='prankpatrol'),
    #path('command/', command.command, name='command'),
]
