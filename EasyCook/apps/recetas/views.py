from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from apps.recetas.forms import RecetaForm
from apps.recetas.models import Receta

def index(request):
    return render(request,'index.html')
#  *******************************************************
#  ****************** CRUD PRINCIPALES********************
#  *******************************************************
class RecetaList(ListView):
    model = Receta
    template_name = 'receta_list.html'
class RecetaCreate(CreateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'receta_form.html'
    success_url = reverse_lazy('recetas:index')
class RecetaUpdate(UpdateView):
    model = Receta
    form_class = RecetaForm
    template_name = 'receta_form.html'
    success_url = reverse_lazy('recetas:receta_listar')
class  RecetaDelete(DeleteView):
    model = Receta
    form_class = RecetaForm
    template_name = 'receta_delete.html'
    success_url = reverse_lazy('recetas:receta_listar')
#  *******************************************************
#  ****************** VISTAS USUARIO *********************
#  *******************************************************

class RecetaListFacil(ListView):
    model = Receta
    template_name = 'receta_listF.html'
class RecetaListSaludable(ListView):
    model = Receta
    template_name = 'receta_listS.html'
class RecetaListVegetariana(ListView):
    model = Receta
    template_name = 'receta_listV.html'
class RecetaListGourmet(ListView):
    model = Receta
    template_name = 'receta_listG.html'