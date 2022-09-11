"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from .views import views,testDB

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.Hello),
    path('index/',views.index),

    path(r'index/add$',testDB.add),
    path(r'index/all',testDB.getAll),
    path(r'index/search$',testDB.getInfoById),
    path(r'index/update',testDB.updateInfo),
    path(r'index/delete',testDB.deleteInfo),

]
