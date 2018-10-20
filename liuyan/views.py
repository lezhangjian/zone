from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views import View
from liuyan.models import LiuyanModels
from django.http import HttpResponseRedirect
# Create your views here.


class IndexView(View):
    def get(self, request):
        liuyans = LiuyanModels.objects.all().order_by('-add_time')
        return render(request, 'text.html', {"liuyans": liuyans})

    def post(self, request):
        # 实例化数据库
        liuyan = LiuyanModels()
        liuyan.name = request.POST.get("name")
        liuyan.message = request.POST.get("message")
        # 保存数据到数据库
        liuyan.save()
        return HttpResponseRedirect('/index/')


class AlbunView(View):
    def get(self, request):
        liuyans = LiuyanModels.objects.all().order_by('-add_time')
        return render(request, 'index-gray.html', {"liuyans": liuyans})

    def post(self, request):
        # 实例化数据库
        liuyan = LiuyanModels()
        liuyan.name = request.POST.get("name")
        liuyan.message = request.POST.get("message")
        # 保存数据到数据库
        liuyan.save()
        return HttpResponseRedirect('/album/')