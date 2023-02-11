"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include

#添加第一个URL，根据Simontest的app里面的views导入
from Simontest.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
# path（路由，视图函数名字）
# comment掉因为已经移到子应用中了
    # path('index/', index)
    #同时添加子应用simontest中所有路径,需要导包include
    path('', include('Simontest.urls'))
]
