from django.shortcuts import render

# Create your views here.


#request 相当于FLASK的路径
#导入request和response

from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    #格式：render(request请求，模板路径名字，)
    
    context={
        'name':'Storm is coming'
    } #context作用是传递数据到html模板
    return render(request, 'Simontest/index.html',context)
    # return HttpResponse('ok')

