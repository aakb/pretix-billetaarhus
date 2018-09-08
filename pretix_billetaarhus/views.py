import json

from django.conf import settings
from django.shortcuts import render


def create_copy_css(request, *args, **kwargs):
    template_name = 'pretix_billetaarhus/css/create-copy.css'
    context = {}
    content_type = 'text/css'

    return render(request, template_name, context, content_type)


def create_copy_js(request, *args, **kwargs):
    template_name = 'pretix_billetaarhus/js/create-copy.js'
    template_event_ids = json.loads(settings.BILLETAARHUS_TEMPLATE_EVENT_IDS) if hasattr(settings, 'BILLETAARHUS_TEMPLATE_EVENT_IDS') else None
    template_event_name_pattern = json.loads(settings.BILLETAARHUS_TEMPLATE_EVENT_NAME_PATTERN) if hasattr(settings, 'BILLETAARHUS_TEMPLATE_EVENT_NAME_PATTERN') else None
    context = {
        'template_event_ids': template_event_ids,
        'template_event_name_pattern': template_event_name_pattern
    }
    content_type = 'text/javascript'

    return render(request, template_name, context, content_type)
