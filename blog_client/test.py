#!/usr/bin/env python
# coding:utf-8

from psutil import cpu_count, virtual_memory, disk_usage
from platform import node
from commands import getoutput
import requests
import json
import re


class service_info(object):

    def __init__(self):
        self.dic = {}

    def get_mem(self):

        mem = int(getoutput("cat /proc/meminfo |grep 'MemTotal'|awk '{print $2}'")) / 1000 / 1000

        return mem

    def get_cpu(self):

        cpu = getoutput("cat /proc/cpuinfo |grep processor|wc -l")

        return cpu

    def get_within(self):

        within = getoutput('hostname -I').split()[0]

        return within

    def get_abroad(self):

        abroad = getoutput('curl -s members.3322.org/dyndns/getip')

        return abroad

    def get_hostname(self):

        name = getoutput("hostname")

        return name

    def get_disk(self):

        disk = getoutput("fdisk -l|grep 'Disk /'|awk '{print $3}'")

        return disk

    def get_service(self):
        service_dic = {}
        data = getoutput("netstat -anplt|grep LISTEN|awk '$4 ~ /:::/{print $4,$NF}'|awk -F':' '{print $NF}'")
        for d in data.split('\n'):
            if d.count('/') > 1:
                sd = getoutput('ps aux|grep %s|grep -v grep' % re.findall('(\d+)/', d.split()[1])[0])
                pn = re.findall('(\w+)/bin', sd)
                if pn == []:
                    service_dic[re.findall('/(\w+)', sd)[-1]] = d.split()[0]
                else:
                    service_dic[pn[0]] = d.split()[0]
            else:
                po, pr, na = d.split()[0], d.split()[1].split('/')[0], d.split()[1].split('/')[1]
                if data.count(na) == 1:
                    service_dic[na] = po
                elif data.count(na) > 1:
                    if 'docker' not in na:
                        sd = getoutput('ps aux|grep -w %s|grep -v grep' % pr)
                        na = re.findall('/(\w+-\w+)\.jar', sd)
                        if na == []:
                            na = re.findall('/(\w+)/bin', sd)
                            service_dic[na[0]] = po
                        else:
                            service_dic[na[0]] = po

        return service_dic

    def main(self):

        self.dic['meminfo'] = self.get_mem()
        self.dic['cpuinfo'] = self.get_cpu()
        self.dic['within'] = self.get_within()
        self.dic['abroad'] = self.get_abroad()
        self.dic['hostname'] = self.get_hostname()
        self.dic['diskinfo'] = self.get_disk()
        self.dic['service_port'] = str(self.get_service())
        return self.dic

    def task_cmd(self):
        task_cmd = {}
        task_cmd['name'] = self.get_hostname()
        task_cmd['ip'] = self.get_within()
        return task_cmd

    def post_data(self,ip):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = self.main()
        url = 'http://%s/assets/post_service/' % ip
        cent = requests.post(url, data=json.dumps(data), headers=headers)
        print cent.content

    def task_data(self,ip):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = self.task_cmd()
        url = 'http://%s/tasks/remote_task_set/' % ip
        cent = requests.post(url, data=json.dumps(data), headers=headers)
        print cent.content



service_info().post_data('192.168.100.5:12307')
try:
    import ansible
    service_info().task_data('192.168.100.5:12307')
except ImportError:
    pass


__author__ = 'yangyang'