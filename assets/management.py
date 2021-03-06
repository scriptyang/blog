from django.db.models.signals import post_migrate
from models import service_info,Blog_settings
import string

def init_data(sender, **kwargs):
    if sender.name == 'assets' :
        n = 1
        for x in string.ascii_lowercase:
            service_info.objects.get_or_create(sn=x,name='192.168.0.'+str(n))
            n += 1

post_migrate.connect(init_data)
