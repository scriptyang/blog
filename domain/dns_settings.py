#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yangyang'

'''
pip install aliyun-python-sdk-ecs
pip install aliyun-python-sdk-httpdns==2.1.0
pip install aliyun-python-sdk-domain
pip install aliyun-python-sdk-alidns
'''

from aliyunsdkcore.client import AcsClient
# from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
# from aliyunsdkecs.request.v20140526 import StopInstanceRequest
from aliyunsdkalidns.request.v20150109 import DescribeDomainsRequest, DescribeDomainRecordsRequest, \
    UpdateDomainRecordRequest, AddDomainRecordRequest, DeleteDomainRecordRequest, SetDomainRecordStatusRequest
import json


class AliDomain(object):

    def __init__(self, aki, aks, DomainName):
        self.client = AcsClient(
            aki,
            aks
        )
        self.DomainName = DomainName
        self.DomainRecords = DescribeDomainRecordsRequest.DescribeDomainRecordsRequest()
        self.DomainRecords.set_accept_format('json')
        self.DomainRecords.set_DomainName(DomainName)
        self.DomainRecordsJson = json.loads(self.client.do_action_with_exception(self.DomainRecords))

    # 获取二级域名
    def list_domain(self):
        DomainList = DescribeDomainsRequest.DescribeDomainsRequest()
        DomainList.set_accept_format('json')
        DNSListJson = json.loads(self.client.do_action_with_exception(DomainList))
        for i in DNSListJson['Domains']['Domain']:
            print i['DomainName']
        # print DNSListJson

    # 获取域名信息（修改自己的DomainName）
    def list(self):
        li_to = []
        for x in self.DomainRecordsJson['DomainRecords']['Record']:

            RR = x['RR']
            Type = x['Type']

            Value = x['Value']

            Status = x['Status']
            n = {"Host":RR,"Type":Type,"Value":Value,"Status":Status}
            li_to.append(n)
        return li_to

    # 更新域名解析（修改的域名DomainName，和要修改的hostname，修改成hostname_new，解析的类型Types，解析的地址IP）
    def edit(self, hostname, hostname_new, Types, IP):

        for x in self.DomainRecordsJson['DomainRecords']['Record']:
            if hostname == x['RR']:
                RecordId = x['RecordId']
                UpdateDomainRecord = UpdateDomainRecordRequest.UpdateDomainRecordRequest()
                UpdateDomainRecord.set_accept_format('json')
                UpdateDomainRecord.set_RecordId(RecordId)
                UpdateDomainRecord.set_RR(hostname_new)
                UpdateDomainRecord.set_Type(Types)
                UpdateDomainRecord.set_TTL('600')
                UpdateDomainRecord.set_Value(IP)
                UpdateDomainRecordJson = json.loads(self.client.do_action_with_exception(UpdateDomainRecord))
                return UpdateDomainRecordJson

    # 增加域名解析
    def add(self, hostname, Types, IP):
        AddDomainRecord = AddDomainRecordRequest.AddDomainRecordRequest()
        AddDomainRecord.set_DomainName(self.DomainName)
        AddDomainRecord.set_RR(hostname)
        AddDomainRecord.set_Type(Types)
        AddDomainRecord.set_TTL('600')
        AddDomainRecord.set_Value(IP)
        AddDomainRecordJson = json.loads(self.client.do_action_with_exception(AddDomainRecord))
        return AddDomainRecordJson

    # 删除域名解析
    def delete(self, hostname):

        for x in self.DomainRecordsJson['DomainRecords']['Record']:
            if hostname == x['RR']:
                RecordId = x['RecordId']
                DeleteDomainRecord = DeleteDomainRecordRequest.DeleteDomainRecordRequest()
                DeleteDomainRecord.set_RecordId(RecordId)
                DeleteDomainRecordJson = json.loads(self.client.do_action_with_exception(DeleteDomainRecord))
                return DeleteDomainRecordJson

    # 设置域名解析
    def set(self, hostname, status):

        for x in self.DomainRecordsJson['DomainRecords']['Record']:
            if hostname == x['RR']:
                RecordId = x['RecordId']
                SetDomainRecord = SetDomainRecordStatusRequest.SetDomainRecordStatusRequest()
                SetDomainRecord.set_accept_format('json')
                SetDomainRecord.set_RecordId(RecordId)
                SetDomainRecord.set_Status(status)
                SetDomainRecordJson = json.loads(self.client.do_action_with_exception(SetDomainRecord))
                return SetDomainRecordJson


if __name__ == '__main__':
    aki = 'LTAIEaNLSsrvKnNi'
    aks = 'RmtJURUpnhFbw9EextTCdUoA71Hikp'
    DomainName = 'bjtraveler.club'
    AliDomain(aki, aks, DomainName).list()
    # 结果： 显示域名解析记录

    # 修改域名
    # AliDomain(aki,aks,DomainName).edit('blog', 'www', 'A', '172.96.220.224')
    # 返回{u'RecordId': u'4140838054151168', u'RequestId': u'2281EAF8-2910-4AD9-86A8-3DF28B5DAA36'} 可进行判断

    # 增加域名
    # AliDomain(aki,aks,DomainName).add('test', 'A', '172.96.220.224')
    # 返回{u'RecordId': u'4140838054151168', u'RequestId': u'2281EAF8-2910-4AD9-86A8-3DF28B5DAA36'} 可进行判断

    # 删除域名
    # AliDomain(aki,aks,DomainName).delete('test')
    # 返回{u'RecordId': u'4140838054151168', u'RequestId': u'2281EAF8-2910-4AD9-86A8-3DF28B5DAA36'} 可进行判断

    # 关闭域名解析
    # AliDomain(aki,aks,DomainName).set('www', 'DISABLE')
    # 关闭

    # 开启域名解析
    # AliDomain(aki,aks,DomainName).set('www', 'ENABLE')
    # 开启

    # 列出域名
    # AliDomain(aki,aks,DomainName).list_domain()
    # 结果： 显示一级域名