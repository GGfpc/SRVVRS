from django.conf.urls import url
from . import views


app_name = 'projs'

urlpatterns = [
    url(r'^projetos$', views.lista_de_projs,name='lista_de_projectos'),
    url(r'^(?P<post_id>[0-9]+)/voto/$', views.voto, name='voto'),
    url(r'^(?P<post_id>[0-9]+)/detalheBlog/$', views.detalheBlog, name='detalheBlog'),
    url(r'^(?P<post_id>[0-9]+)/comentario/$', views.comentario, name='comentario'),
    url(r'^$', views.home, name='home'),
    url(r'^logging$', views.logging, name='logging'),
    url(r'^(?P<post_id>[0-9]+)/detalheProj/$', views.detalheProj, name="detalheProj"),
    url(r'^dash$',views.dashboard, name='dashboard'),
    url(r'^(?P<comment_id>[0-9]+)/apagaComment/$', views.apagaComment, name="apagaComment"),
    url(r'^(?P<empregado_id>[0-9]+)/apagaEmpreagado/$', views.apagaEmpregado, name="apagaEmpregado"),
    url(r'^(?P<post_id>[0-9]+)/apagaProj/$', views.apagaProj, name="apagaProj"),
    url(r'^(?P<user_id>[0-9]+)/apagaUser/$', views.apagaUser, name="apagaUser"),
    url(r'^(?P<post_id>[0-9]+)/apagaBlogPost/$', views.apagaBlogPost, name="apagaBlogPost"),
    url(r'^criaproj', views.criaProj,name='criaProj'),
    url(r'^criauser', views.criaUser,name='criaUser'),
    url(r'^criaempregado', views.criaEmpregado,name='criaEmpregado'),
    url(r'^criablogpost', views.criaBlogPost,name='criaBlogPost'),
    url(r'^blog$', views.blog, name='blog')

]