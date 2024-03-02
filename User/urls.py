from django.urls import path
from User import views

# 1. 写路由 /123 去返回一个文本123
# 2. 编写视图
urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dash, name='Dashboard'),
    path('profile/', views.profile, name='profile'),
    path('login',views.login, name='login')
]