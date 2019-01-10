import requests
import json

def task_data(ip):
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {'sn':'kvm000','name':'winc00031','l2tp':'172.2.0.14','ssl':'172.1.0.31'}
    url = 'http://%s/assets/post_service/' % ip
    cent = requests.post(url, data=json.dumps(data), headers=headers)
    print cent.content

task_data('192.168.12.7')
