
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('vendor/register/', views.vendor_register, name='register'),
]
