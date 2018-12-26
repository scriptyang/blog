from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$',login_index),
    url(r'login_veri/$',login_veri,name='login_veri'),
    url(r'index/$',index,name='login_index'),
    url(r'logout/$',logout,name='logout')
]