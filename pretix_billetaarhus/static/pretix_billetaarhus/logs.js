(function($) {
    $(function() {
        var modal = $('#billet-aarhus-log-data-modal')
        // https://stackoverflow.com/a/11788713
        modal.appendTo('body')

        modal
            .on('show.bs.modal', function (event) {
                var button = $(event.relatedTarget)
                var title = button.data('log-title')
                var data = button.data('log-data')
                modal.find('.modal-title').text(title)
                modal.find('.modal-body .log-data').html(JSON.stringify(data, null, 2))
            })
            .on('shown.bs.modal', function (event) {
                // https://stackoverflow.com/a/11788713
                modal.find('.modal-backdrop').css({zIndex: -1})
            })
    })
}(jQuery))
