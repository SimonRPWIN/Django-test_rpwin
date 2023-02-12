from django.shortcuts import render

# Create your views here.


#request 相当于FLASK的路径
#导入request和response

from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    #格式：render(request请求，模板路径名字，)
    
    # context={
    #     'name':'Storm is coming'
    # } #context作用是传递数据到html模板
    return render(request, 'Simontest/index.html')
    # return HttpResponse('ok')

from Simontest.models import BookInfo,PeopleInfo

#增加数据
# BookInfo.objects.create(
#     name='测试入门',
#     pub_date = '2020-1-1',
#     readcount = 100,)

#修改数据
# BookInfo.objects.filter(id=5).update(name='爬虫入门')

from django.db.models import F
# 以两个条件查询
# BookInfo.objects.filter(readcount__gte=F('commentcount'))

# PeopleInfo.objects.filter(book__name__contains='天')

# 查询id为1的书的所有人物信息。
# PeopleInfo.objects.filter(book__id=1)

def create(request):
    return HttpResponse('create')