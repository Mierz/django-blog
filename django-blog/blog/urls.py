from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_url>[a-z]+)$', views.view, name='view'),
    url(r'^page/(?P<page_url>[a-z]+)$', views.page, name='page'),
    url(r'^category/(?P<category_id>[0-9]+)$', views.category, name='category'),
]