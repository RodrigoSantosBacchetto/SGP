from django.shortcuts import render_to_response, render, HttpResponseRedirect, HttpResponse, RequestContext, get_object_or_404
from administracion.forms import UsuarioForm, ProyectoForm, UsuarioModForm, UsuarioDelForm, FaseForm, RolForm, AsignarRol
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group, Permission
from administracion.models import Proyecto, Fase

@login_required(login_url='/iniciar_sesion')
def desarrollo(request):
    """

    :param request:
    :return:

    Vista que muestra el contenido privado del modulo de desarrollo

    | Recibe como parametro un request y retorna la pagina web desarrollo.html donde se muestra la
    | lista de proyectos del sistema si el usuario posee los permisos correspondientes

    * Variables
        -   lista_proyectos: es la lista de proyectos existentes en el sistema
        -   usuario: es el usuario logueado
    """
    lista_proyectos = Proyecto.objects.all()
    usuario = request.user
    return render_to_response('desarrollo.html', {'lista_proyectos': lista_proyectos, 'usuario': usuario},
                              context_instance=RequestContext(request))