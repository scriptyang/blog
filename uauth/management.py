from django.db.models.signals import post_migrate
from django.contrib.auth.models import User


def init_user(sender, **kwargs):
    if sender.name == 'uauth' :
        User.objects.create_superuser(username='admin', password='admin', email='')


post_migrate.connect(init_user)