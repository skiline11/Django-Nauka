from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', views.login, name='login'),  #korzystamy z widoków z django.contrib.auth
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),  #korzystamy z widoków z django.contrib.auth
    url(r'', include('blog.urls')),
]
