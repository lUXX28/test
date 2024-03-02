"""tango_with_django_project URL Configuration

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
from index import views

# 1. 创建一个新的应用User，访问两个url 1./dashboard return welcome dashboard
#                                 2./profile => return : this is the profile
# tips: Using python manage.py to create the new app.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', include('index.urls')),
    path('article/', include('Article.urls')),
    path('user/', include('User.urls'))

]
