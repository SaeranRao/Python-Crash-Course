"""为应用程序users的URL模式。"""
from django.urls import path,include

app_name = 'users'
urlpatterns = [
    #默认的身份验证URL
    path('',include('django.contrib.auth.urls')),
]
