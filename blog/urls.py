from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.lista_postow, name='lista_postow'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.szczegoly_postu, name='szczegoly_postu'),
    url(r'^post/nowy/$', views.nowy_post, name='nowy_post'),
    url(r'^post/(?P<pk>[0-9]+)/edytuj/$', views.edycja_postu, name='edycja_postu'),
    url(r'^robocze/$', views.lista_wersji_roboczych, name='lista_wersji_roboczych'),
    url(r'^post/(?P<pk>\d+)/publikuj/$', views.publikacja_postu, name='publikacja_postu'),
    url(r'^post/(?P<pk>\d+)/usun/$', views.usuwanie_postu, name='usuwanie_postu'),
    url(r'^post/(?P<pk>\d+)/komentarz/$', views.dodawanie_komentarza, name='dodawanie_komentarza'),
    url(r'^komentarz/(?P<pk>\d+)/zatwierdz/$', views.zatwierdzanie_komentarza, name='zatwierdzanie_komentarza'),
    url(r'^komentarz/(?P<pk>\d+)/usun/$', views.usuwanie_komentarza, name='usuwanie_komentarza'),
]
