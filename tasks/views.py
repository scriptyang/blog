# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task_info
from .models import local_cmd
from .models import remote_cmd
from .models import re_cm
from django.core.cache import cache
import threading
from commands import getoutput
import subprocess,time

def task_list(request):
    head_info = "工单"
    user = request.session.get('userid')
    local_da = list(local_cmd.objects.values())
    remote_da = list(remote_cmd.objects.values())
    remote_task = list(re_cm.objects.values())
    return render(request,'tasks.html',locals())


def task_run(request):

    result = request.POST.get('level')

    def local_task(cmd):
        a = ''
        cache.set('name','程序开始运行。。。')
        subprocess.Popen('%s >/tmp/a 2>&1'% cmd, shell=True)

        time.sleep(5)
        cache.delete('name')
        getoutput('echo "程序执行完成状态：SUCCESS">>/tmp/a')

    t = threading.Thread(target=local_task,args=(result,))
    t.setDaemon(True)
    t.start()

    start_time = time.ctime()
    ti = Task_info.objects.create(command=result,user=request.session.get('userid'), start_time=start_time,content='1')

    cache.set('task_id',ti.id)
    return HttpResponse('ok')

def redis_test(request):
    d = ''
    for x in open('/tmp/a').readlines():
        d += '<p style="text-align:left;">%s</p>' % x
    cache.set('content', d)

    return HttpResponse(d)

def set_content(request):
    cond = request.POST.keys()[0]
    cache.set('content',cond)

    return HttpResponse('ok')

def remote_task_set(request):

    if request.POST.get('remark') == 'local':

        local_cmd.objects.create(cmd=request.POST.get('cmd'))

    elif request.POST.get('remark') == 'remote':

        re_cm.objects.create(cmd=request.POST.get('cmd'))

    return HttpResponse('ok')

def remote_task(request):

    cmd = request.POST.get('cmd')
    addr = request.POST.get('addr')
    print cmd,addr
    return HttpResponse('ok')

# Create your views here.
