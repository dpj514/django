from django.shortcuts import render,render_to_response
from news1.models import News
from django.http import HttpResponse
import pymysql
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def index(request):
    allnews = News.objects.all()
    paginator = Paginator(allnews,8)
    page = request.GET.get('page')
    try:
        allnews = paginator.page(page)
    except PageNotAnInteger:
        allnews = paginator.page(1)
    except EmptyPage:
        allnews = paginator.page(paginator.num_pages)
    return render_to_response('index.html',{'allnews':allnews})
def news(request,id):
    i = int(id)
    a = News.objects.all()[i-1]
    return render_to_response('news.html',{'a':a})

