from django.contrib import admin
from django.urls import path, include
from .views import post_detail, layout1, layout2, layout5

urlpatterns = [
    path('layout1/', layout1, name='post_list'),
    path('layout2/', layout2, name='post_list'),
    path('layout5/', layout5, name='post_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
]
