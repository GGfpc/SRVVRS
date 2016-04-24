from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.lista_de_projs,name='lista_de_projectos')

]