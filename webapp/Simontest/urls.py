from django.urls import path
from Simontest.views import index

urlpatterns = [
# path（路由，视图函数名字）
    path('index/', index)

]