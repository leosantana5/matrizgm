"""
Scalper URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('Scalper.apps.base.urls')),
]