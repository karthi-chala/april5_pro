from django.contrib import admin
from django.urls import path
import os
from app1 import views
app_name='app1'

urlpatterns = [
    path('',views.index,name='index'),
    
    path('sample/',views.sample_app1,name='sample_app1'),
]