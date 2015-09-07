from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<post_id>[0-9]+)/view/$', views.view, name='view'),
    url(r'^(?P<page_id>[0-9]+)/page/$', views.page, name='page')
]