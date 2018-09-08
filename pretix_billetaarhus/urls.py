from django.conf.urls import url

from .views import create_copy_css, create_copy_js

urlpatterns = [
    url(r'^_pretix_billetaarhus/css/create-copy.css$', create_copy_css, name='create_copy_css'),
    url(r'^_pretix_billetaarhus/js/create-copy.js$', create_copy_js, name='create_copy_js')
]
