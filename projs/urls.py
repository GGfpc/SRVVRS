from django.conf.urls import url
from . import views


app_name = 'projs'

urlpatterns = [
    url(r'^$', views.lista_de_projs,name='lista_de_projectos'),
    url(r'^(?P<post_id>[0-9]+)/voto/$', views.voto, name='voto'),
    url(r'^home$', views.home, name='home')
]