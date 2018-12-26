from django.conf.urls import url
from .views import *

urlpatterns = [
    url('task_list/$', task_list, name='task_list'),
    url('task_run/$', task_run, name='command'),
    url('redis_test/$',redis_test,name='redis_test'),
    url('set_content/$',set_content),
    url('remote_task/$', remote_task, name='remote_task'),
    url('remote_task_set/$',remote_task_set,name='remote_task_set'),
]

