from django.conf.urls import url
from . import views


app_name = 'projs'

urlpatterns = [
    url(r'^$', views.lista_de_projs,name='lista_de_projectos'),
    url(r'^(?P<post_id>[0-9]+)/voto/$', views.voto, name='voto'),
    url(r'^(?P<post_id>[0-9]+)/comentario/$', views.comentario, name='comentario'),
    url(r'^home$', views.home, name='home'),
    url(r'^logging', views.logging, name='logging'),
    url(r'^(?P<post_id>[0-9]+)/detalheProj/$', views.detalheProj, name="detalheProj"),
]