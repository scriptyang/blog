#coding:utf-8

from tasks.models import Task_info
from django.shortcuts import render
from django.http import HttpResponse
import json
from assets.models import service_info as service_data
from django.core.cache import cache
from django.shortcuts import render_to_response
from assets.models import Domain_info
from .dns_settings import AliDomain
from blog.settings import AKI,AKS,DomainName

import sys
reload(sys)
sys.setdefaultencoding('utf8')


def table(request):
    user = request.session.get('userid')
    head_info = "服务器信息"
    return render(request, 'service_info.html', locals())

def post_service(request):

    post_service = eval(request.POST.keys()[0])
    se = service_data.objects.filter(hostname=post_service['hostname']).count()
    if se > 0:
        sd = service_data.objects.get(hostname=post_service['hostname'])
        sd.abroad = post_service['abroad']
        sd.within = post_service['within']
        sd.meminfo = post_service['meminfo']
        sd.cpuinfo = post_service['cpuinfo']
        sd.diskinfo = post_service['diskinfo']
        sd.service_port = post_service['service_port']
        sd.save()
    else:
        service_data.objects.create(**post_service)

    return HttpResponse('ok')

def drop_tables(request):
    #删除 数据库操作
    if request.method == "POST":
        name = request.POST.get('name')
        if name == 'tasks':
            Task_info.objects.get(id=request.POST.get('id')).delete()
            return HttpResponse('ok')

        if name == 'service_info':

            service_data.objects.get(id=request.POST.get('id')).delete()
            return HttpResponse('ok')

    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return HttpResponse('ok')
    else:
        return HttpResponse('不允许如此操作！！！')

def table_data(request):
    name = request.GET.get('name')

    if name == 'service_info':
        data2 = list(service_data.objects.values())

        for s in data2:
            phtml = '<p>'
            swal = '<div class="content">'
            swal += '<div class="order"><span class="line"></span><span class="txt">系统信息</span><span class="line"></span></div>'

            swal +=  '<button class ="btn btn-wd btn-info" style="line-height:22px" > 主机名称 ： % s </button>' % s['hostname']

            swal += '<button class ="btn btn-wd btn-info" style="line-height:22px" > cpu ： % s </button>' % s['cpuinfo']
            swal += '<button class ="btn btn-wd btn-info" style="line-height:22px" > 内存 ： % s </button>' % s['meminfo']
            swal += '<button class ="btn btn-wd btn-info" style="line-height:22px" > 磁盘空间 ： % s (GB) </button>' % s[
                'diskinfo']
            swal += '<button class ="btn btn-wd btn-info" style="line-height:22px" > 外网地址 ： % s </button>' % s[
                'abroad']
            swal += '<button class ="btn btn-wd btn-info" style="line-height:22px" > 内网地址 ： % s </button>' % s[
                'within']
            swal += '<button class ="btn btn-wd btn-info" style="line-height:22px" > 备注信息 ： % s </button>' % s[
                'remark']
            swal += '</br> <div class="order"><span class="line"></span><span class="txt">服务端口</span><span class="line"></span></div>'
            if s['service_port']:
                for k,v in eval(s['service_port']).items():
                    phtml += ' %s : %s ' % (k,v)
                    swal += '<button class="btn btn-wd btn-info" style="line-height:22px"> %s ：%s </button>' % (k,v)
                phtml += '</p>'
                swal += '</div>'
            else:
                phtml += '</p>'
                swal += '</div>'

            s['p_info'] = phtml
            s['swal'] = swal

        data2 = json.dumps(data2)
        return HttpResponse(str(data2))

    elif name == 'task_info':
        d1 = list(Task_info.objects.values())
        data2 = json.dumps(d1)
        return HttpResponse(str(data2))
    elif  name == 'mydiv':

        ta = Task_info.objects.get(id=cache.get('task_id'))
        ta.content = cache.get('content')
        ta.save()

        return HttpResponse(ta.content)

def folder_tree(request):
    data = [{
        "目录": "第一级"
    }]
    d2 = json.dumps(data)
    return HttpResponse(str(d2))

def service_edit(request):
    user = request.session.get('userid')
    id,remark = request.POST.get('id'),request.POST.get('remark')
    sd = service_data.objects.get(id=id)
    sd.remark = remark
    sd.save()
    return HttpResponse('更新完成')

def user_sett(request):
    user = request.session.get('userid')
    head_info = '用户设置'

    return render(request,'service_settings.html',locals())

def error_page(request):

    return render_to_response('404.html')


def domain(request):
    user = request.session.get('userid')
    head_info = '域名设置'
    if request.method == "POST":
        domain = Domain_info.objects.all()
        ad = AliDomain(AKI, AKS, DomainName)
        Ali = ad.list()
        if domain.count() != len(Ali):
            for l in Ali:
                l['Host'] = l['Host']+'.'+DomainName
                Domain_info.objects.create(**l)

        da = list(Domain_info.objects.values())
        da2 = json.dumps(da)
        return HttpResponse(str(da2))

    else:

        return render(request,'domain.html',locals())

# Create your views here.
