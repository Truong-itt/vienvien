from django.contrib import admin
from django.urls import path, include
from .views import post_detail, layout1, layout2, layout5

urlpatterns = [
    path('layout1/', layout1, name='layout1'),
    path('layout2/', layout2, name='layout2'),
    path('layout5/', layout5, name='layout3'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    
]
