#coding:utf-8
from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from assets.models import service_info
try:
    from domain.models import Domain_info
except:
    domain = '无'
from tasks.models import Task_info
from .models import login_info

def index(request):
    user = request.session.get('userid')
    head_info = "Dashboard Pro"
    service_num =  service_info.objects.all().count()
    tasks_num = Task_info.objects.all().count()
    if '无' not in domain:
    	Domain_num = Domain_info.objects.all().count()

    login = login_info.objects.values().order_by('-id')[5:]
    if user is None:
        return HttpResponseRedirect('/')
    return render(request, 'index.html', locals())

def login_index(request):
    if request.META.get('HTTP_REFERER') is None:
        request.session['login_status'] = '1'
    return render(request,'login.html')

def login_veri(request):

    user = request.POST.get('username')
    passwd = request.POST.get('password')
    dic = {"addr":request.META['REMOTE_ADDR'],"user":user}
    login_info.objects.create(**dic)

    if request.method == 'POST':

        user = auth.authenticate(username=user,password=passwd)
        if user is not None and user.is_active:
            request.session['userid'] = str(user)
            return HttpResponseRedirect("/index/")
        else:
            request.session['login_status'] = 'false'
            return HttpResponseRedirect('/')

def logout(request):
    del request.session['userid']
    return HttpResponseRedirect("/index/")

# Create your views here.
