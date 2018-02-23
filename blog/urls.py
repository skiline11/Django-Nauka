from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_postow, name='lista_postow'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.szczegoly_postu, name='szczegoly_postu'),
    url(r'^post/nowy/$', views.nowy_post, name='nowy_post'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.edycja_postu, name='edycja_postu')
]