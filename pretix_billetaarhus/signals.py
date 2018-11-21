import json
import re

from django.dispatch import receiver
from pretix.base.signals import auth_get_event_permission_set
from pretix.settings import config


@receiver(auth_get_event_permission_set, dispatch_uid="billetaarhus_auth_get_event_permission_set")
def auth_get_event_permission_set(sender, **kwargs):
    request = kwargs['request']
    eventpermset = request.eventpermset
    user = request.user

    section_name = 'billetaarhus.permissions'
    if config.has_section(section_name):
        for permission in config.options(section_name):
            users = json.loads(config.get(section_name, permission))
            if user.email in users:
                deny = False
                if re.match('[!-]', permission):
                    deny = True
                    permission = permission[1:]
                if deny:
                    eventpermset.discard(permission)
                else:
                    eventpermset.add(permission)
