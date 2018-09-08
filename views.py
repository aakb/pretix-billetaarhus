from django.conf import settings
from django.shortcuts import render


def siteimprove(request, *args, **kwargs):
    template_name = 'pretix_siteimprove/siteimprove.js'
    siteimprove_code = settings.SITEIMPROVE_CODE if hasattr(settings, 'SITEIMPROVE_CODE') else None
    context = {
        'siteimprove_code': siteimprove_code
    }
    content_type = 'text/javascript'

    return render(request, template_name, context, content_type)
