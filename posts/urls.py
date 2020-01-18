from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='list'),
    url(r'^create/$', views.post_create),
    url(r'^details/(?P<id>\d+)/$', views.post_details, name='detail'),
    url(r'^(?P<id>\d+)/edit/$', views.post_update, name='update'),
    url(r'^(?P<id>\d+)/delete/$', views.post_delete),
]
