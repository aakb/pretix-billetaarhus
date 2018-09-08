from django.apps import AppConfig
from django.utils.translation import ugettext_lazy


class PluginApp(AppConfig):
    name = 'pretix_billetaarhus'
    verbose_name = 'billetaarhus'

    class PretixPluginMeta:
        name = ugettext_lazy('billetaarhus')
        author = 'Mikkel Ricky'
        description = ugettext_lazy('billetaarhus')
        visible = False
        version = '1.0.0'

    def ready(self):
        from . import signals  # NOQA


default_app_config = 'pretix_billetaarhus.PluginApp'
