from django.shortcuts import render

# Create your views here.


#request 相当于FLASK的路径
#导入request和response

from django.http import HttpRequest
from django.http import HttpResponse

def index(request):
    
    return HttpResponse('ok')

