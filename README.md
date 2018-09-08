billetaarhus
============

Pretix hacks for billet.aarhus.dk.

1. Append this to `settings.py` (or, preferably, in your custom
   settings file
   (cf. https://docs.djangoproject.com/en/2.0/topics/settings/#designating-the-settings)):

       if config.has_option('billetaarhus', 'template_event_ids'):
           BILLETAARHUS_TEMPLATE_EVENT_IDS = config.get('billetaarhus', 'template_event_ids')
       if config.has_option('billetaarhus', 'template_event_name_pattern'):
           BILLETAARHUS_TEMPLATE_EVENT_NAME_PATTERN = config.get('billetaarhus', 'template_event_name_pattern')

2. Define how to identify your template events in `pretix.cfg`:

       [billetaarhus]
       ;; json list of template event ids
       template_event_ids = [42, 87]
       ;; RegExp pattern (json string) used to identify template events by name
       template_event_name_pattern = "^Standard "

3. Copy
   `pretix_billetaarhus/templates/pretixcontrol/events/create_copy.html`
   to
   `%pretix.datadir%/templates/pretixcontrol/events/create_copy.html`
   or, alternatively, append this line to
   `%pretix.datadir%/templates/pretixcontrol/events/create_copy.html`
   if you've already customized the `create_copy.html` template:

       <script src="{% url 'plugins:pretix_billetaarhus:create_copy_js' %}"></script>

4. Restart Pretix


License
-------

Copyright 2018 Mikkel Ricky

Released under the terms of the Apache License 2.0


.. _pretix: https://github.com/pretix/pretix
.. _pretix development setup: https://docs.pretix.eu/en/latest/development/setup.html
