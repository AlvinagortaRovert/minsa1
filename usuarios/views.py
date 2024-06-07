# usuarios/views.py
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Usuario

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'usuario_list.html'

class UsuarioDetailView(DetailView):
    model = Usuario
    template_name = 'usuario_detail.html'

class UsuarioCreateView(CreateView):
    model = Usuario
    fields = ['dni', 'apellidos', 'nombres', 'correo', 'direccion', 'telefono']
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('usuario-list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    fields = ['dni', 'apellidos', 'nombres', 'correo', 'direccion', 'telefono']
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('usuario-list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuario_confirm_delete.html'
    success_url = reverse_lazy('usuario-list')

# Nueva vista para la página de inicio
def home(request):
    return render(request, 'home.html')

