"""
URL configuration for pqn_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from core import views as core_views

urlpatterns = [
    path('index_base',core_views.index_base,name="index_base"),
    path('',core_views.index,name="index"),
    path('noroeste',core_views.noroeste,name="noroeste"),
    path('noreste',core_views.noreste,name="noreste"),
    path('centro',core_views.centro,name="centro"),
    path('patagonia',core_views.patagonia,name="patagonia"),
    path('austral',core_views.austral,name="austral"),
    path('mar',core_views.mar,name="mar"),
    path('map',core_views.map,name="map"),
    path('admin/', admin.site.urls),
    path('contact',core_views.contact,name="contact"),
]
