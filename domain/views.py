# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .dns_settings import AliDomain
from blog.settings import AKI,AKS,DomainName
from .models import Domain_info

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
