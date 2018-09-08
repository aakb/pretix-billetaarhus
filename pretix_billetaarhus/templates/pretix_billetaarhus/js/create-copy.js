{% load json_util %}

{% if template_event_ids or template_event_name_pattern %}
(function ($) {
    var templateEventIds = {{ template_event_ids|json_encode|safe }},
        templateEventNamePattern = {{ template_event_name_pattern|json_encode|safe }},
        templateEventNameMatcher = templateEventNamePattern ? new RegExp(templateEventNamePattern, 'i') : null;

    $(function() {
        var getEventId = function(el) {
            return parseInt($(el).find('input').val() || 0, 10);
        },
            getEventName = function(el) {
                return $.trim($(el).text());
            },
            stringCompare = function(a, b) {
                return a === b ? 0 : (a < b ? -1 : 1);
            },
            isTemplateEvent = function(el) {
                var id = getEventId(el),
                    name = getEventName(el);

                return (templateEventIds && templateEventIds.indexOf(id) > -1)
                    || (templateEventNameMatcher && templateEventNameMatcher.test(name));
            };

        var $container = $('#id_copy-copy_from_event');

        // Sort template events by
        //   1. importance
        //   2. name
        $container.find('> div').sort(function (a, b) {
            var aId = getEventId(a),
                bId = getEventId(b),
                aName = getEventName(a),
                bName = getEventName(b);
            if (0 === aId) {
                return -1;
            } else if (0 === bId) {
                return 1;
            }

            var aIsTemplateEvent = isTemplateEvent(a),
                bIsTemplateEvent = isTemplateEvent(b);
            if (aIsTemplateEvent && bIsTemplateEvent) {
                return stringCompare(aName, bName);
            } else
                if (aIsTemplateEvent) {
                    return -1;
                } else if (bIsTemplateEvent) {
                    return 1;
                }

            return stringCompare(aName, bName);
        }).detach().appendTo($container);

        $('<link/>', {
            rel: 'stylesheet',
            href: '{% url 'plugins:pretix_billetaarhus:create_copy_css' %}'
        }).appendTo('head');
        $('#id_copy-copy_from_event > div').each(function() {
            if (isTemplateEvent(this)) {
                $(this).addClass('template-event');
            }
        });
    });
}(jQuery));
{% endif %}
