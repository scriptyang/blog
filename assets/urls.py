from django.conf.urls import url
from .views import *

urlpatterns = [
    url('table/$',table,name='bootstrap_table'),
    url('table_data/$',table_data,name='table_data'),
    url('drop_tables/$',drop_tables,name='drop_tables'),
    url('service_edit/$',service_edit,name='service_edit'),
    url('folder_tree/$',folder_tree,name='folder_tree'),
    url('post_service/$',post_service),
    url('settings/$',user_sett,name='user_sett'),

]

handler404 = error_page
