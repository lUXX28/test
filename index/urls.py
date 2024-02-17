from django.contrib import admin
from django.urls import path
from index import views

# 1. 写路由 /123 去返回一个文本123
# 2. 编写视图
urlpatterns = [
    path('user', views.user, name='user'),
    path('123', views.index, name='index')
]