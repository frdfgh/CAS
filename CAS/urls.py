"""CAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from .main import views
from django.conf.urls.static import static
from CAS import settings

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('', views.index, name='mainPage'),
                  path('logout/', views.logoutView, name='logoutPage'),
                  path('login/', views.loginView, name='loginPage'),
                  path('changepass/', views.index, name='WhatToChnagePass'),
                  path('changepass/<slug>', views.index, name='ChangePass'),
                  #path('payment/', views.paymentView, name='paymentPage'),
              ] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns += [
#     path('users/', include('django.contrib.auth.urls')),
# ]