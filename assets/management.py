from django.db.models.signals import post_migrate
from models import service_info,Blog_settings
import string

def init_user(sender, **kwargs):
    if sender.name == 'assets' :
        n = 1
        for x in string.ascii_lowercase:
            service_info.objects.get_or_create(hostname=x,within='192.168.0.'+str(n))
            n += 1

        dic = {'Aki': 'a', 'Aks': 'sd', 'Domain_name': 'a.com', 'server': 'div,div'}
        Blog_settings.objects.create(**dic)

post_migrate.connect(init_user)