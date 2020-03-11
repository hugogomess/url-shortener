from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<shortened_url>[0-9a-zA-Z]+)/$', views.url_redirect, name='url_redirect')
]