# -*- coding:utf-8 -*-

import json
import logging
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,render_to_response,redirect
from django.conf import settings
from develop_app.models import *
from django.core import serializers
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger

# Create your views here.


#设置日志对象
logger = logging.getLogger('develop_app.views')


#设置项目全局变量
def global_setting(request):

    #网站title
    SITE_TITLE = settings.SITE_TITLE
    #网站brand
    SITE_BRAND = settings.SITE_BRAND
    #分页每页默认条数
    per_page = settings.PER_PAGE

    return locals()


#登录页
def login(request):
    return render(request,'login.html')

#注销登录
def logout(request):
    # 方式1
    # request.session.clear()

    #方式2
    try:
        logout(request) #logout
    except Exception as e:
        print (e)
    return HttpResponseRedirect('/login')


def index(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username','')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                user.backend = 'django.contrib.auth.backends.ModalBackEnd'
                auth.login(request,user)
                return render(request, "index.html")
            else:
                return render(request, "login.html")
        else:
            return render(request,"login.html")
    except:
        return render(request, "login.html")


def idc(request):

    # 获取GET请求的参数，得到当前页码。若没有该参数，默认为1
    current_page = request.GET.get("page", 1)
    data_list = Idc.objects.all()

    #从settings中获取分页默认条数
    page = settings.PER_PAGE
    pages = Paginator(data_list,page)  # 6个对象为1页，这个参数可以写在settings.py里面
    data_list = pages.page(current_page)  # 获得当前页的数据

    return render_to_response('idc.html', locals())

def addidc(request):
    try:
        print ('request.POST---->',request.POST)
        if request.method == 'POST':
            name = request.POST.get('name')
            address = request.POST.get('address')
            idc_info = Idc(name=name,address=address)
            idc_info.save()
            return HttpResponse('ok')
        else:
            pass
    except Exception as e:
        print (str(e))

def deleteidc(request):
    try:
        print ('request.GET---->',request.GET)
        if request.method == 'GET':
            id = request.GET.get('id')
            Idc.objects.filter(id=id).delete()
            return HttpResponseRedirect('/idc/')
    except Exception as e:
        print (str(e))

def editidc(request):
    try:
        if request.method == 'GET':
            id = request.GET.get('id')
            idc = Idc.objects.all().filter(id=id)
            #对queryset对象进行序列
            data = serializers.serialize("json", idc)
            res = {'code':0,'idc':data}
            return HttpResponse(json.dumps(res))
        else:
            pass
    except Exception as e:
        print (str(e))


#更新IDC信息,只允许更新idc地址
def updateidc(request):
    try:
        if request.method == 'POST':
            id = request.POST.get('id')
            address = request.POST.get('address')
            Idc.objects.filter(id=id).update(address=address)
            return HttpResponse('ok')
        else:
            return HttpResponse('error')
    except Exception as e:
        print (str(e))

def server(request):
    try:
        idc_list = Idc.objects.all()
        server_list = Server.objects.all()
    except Exception as e:
        pass
    return render(request, "server.html", locals())

def addserver(request):
    try:
        if request.method == 'POST':
            hostname = request.POST['hostname']
            ip = request.POST['ip']
            idc = request.POST['idc']
            cabinet = request.POST['cabinet']
            remark = request.POST['remark']
            server = Server( hostname=hostname,ip=ip, idc=idc, cabinet=cabinet, remark=remark)
            server.save()
            return HttpResponse('ok')
        else:
            pass
    except Exception as e:
        print (str(e))

def delserver(request):
    try:
        if request.method == 'GET':
            id = request.GET.get('id')
            Server.objects.filter(id=id).delete()
            return HttpResponseRedirect('/server/')
    except Exception as e:
        print (str(e))

def editserver(request):
    try:
        if request.method == 'GET':
            id = request.GET.get('id')
            server = Server.objects.all().filter(id=id)
            #对queryset对象进行序列
            data = serializers.serialize("json", server)
            res = {'code':0,'server':data}
            return HttpResponse(json.dumps(res))
        else:
            pass
    except Exception as e:
        print (str(e))

#更新主机信息只允许更新IDC\机柜信息\备注
def updateserver(request):
    try:
        if request.method == 'POST':
            print ('request.POST--->',request.POST)
            id = request.POST.get('id')
            idc = request.POST.get('idc')
            cabinet = request.POST.get('cabinet')
            remark = request.POST.get('remark')
            Server.objects.filter(id=id).update(idc=idc,cabinet=cabinet,remark=remark)
            return HttpResponse('ok')
        else:
            return HttpResponse('error')
    except Exception as e:
        print (str(e))

