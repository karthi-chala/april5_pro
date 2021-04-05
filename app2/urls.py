from django.contrib import admin
from django.urls import path
import os
from app2 import views
app_name='app2'

urlpatterns = [
    path('',views.index,name='index'),
    path('sample/',views.sample_app2,name='sample_app2'),
]