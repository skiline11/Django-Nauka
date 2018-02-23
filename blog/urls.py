from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.lista_postow, name='lista_postow'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.szczegoly_postu, name='szczegoly_postu'),
]