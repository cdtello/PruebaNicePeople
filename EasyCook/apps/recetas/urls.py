from django.conf.urls import patterns, include, url
from django.contrib import admin
from EasyCook import settings

from apps.recetas.views import index, RecetaCreate, RecetaList, RecetaUpdate, RecetaDelete
from apps.recetas.views import RecetaListFacil, RecetaListSaludable, RecetaListVegetariana, RecetaListGourmet

from django.contrib.auth.views import login, logout_then_login
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
   
    
    url(r'login$',login,{'template_name':'login.html'},name='login'),
    url(r'logout$',logout_then_login,name='logout'),


    url(r'^$', index, name='index'),
    url(r'nuevo$', login_required(RecetaCreate.as_view()), name='receta_crear'),
    url(r'listar$', login_required(RecetaList.as_view()), name='receta_listar'),
    url(r'editar/(?P<pk>\d+)/$', login_required(RecetaUpdate.as_view()), name='receta_editar'),
    url(r'eliminar/(?P<pk>\d+)/$', login_required(RecetaDelete.as_view()), name='receta_eliminar'),

    url(r'listarF$', RecetaListFacil.as_view(), name='receta_listarF'),
    url(r'listarS$', RecetaListSaludable.as_view(), name='receta_listarS'),
    url(r'listarV$', RecetaListVegetariana.as_view(), name='receta_listarV'),
    url(r'listarG$', RecetaListGourmet.as_view(), name='receta_listarG'),

    url(r'^media/(?P<path>.*)/$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    
)
