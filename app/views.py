# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
from .models import Usuario
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS
from app.models import Departamento
from app.models import Ciudad
from app.models import ListaEscolaridad
from app.models import ListaEstrato
from app.models import ListaGenero
from .validators import FormRegistroValidator, FormLoginValidator


# Create your views here.

def index(request):
    return render(request, 'index.html')


def registrousu(request):
    error = False
    validator = Validator(request.POST)

    if request.method == 'POST':
        usuario = Usuario()
        usuario.first_name = request.POST['nombre']
        usuario.last_name = request.POST['apellidos']
        usuario.username = request.POST['cedula']
        usuario.email = request.POST['email']
        usuario.password = make_password(request.POST['password'])
        # TODO: ENviar correo electronico para confirmar cuenta
        usuario.is_active = True
        usuario.save()
    else:
        return render_to_response('registrousu.html', {'error': validator.getMessage()},
                                  context_instance=RequestContext(request))
    # Agregar el usuario a la base de datos
    return render_to_response('registrousu.html', context_instance=RequestContext(request))


def login(request):
    """view del login
	    """
    # Verificamos que los datos lleguen por el methodo POST

    if request.method == 'POST':
        # Cargamos el formulario (ver forms.py con los datos del POST)
        validator = FormLoginValidator(request.POST)
        # Verificamos que los datos esten correctos segun su estructura

        if validator.is_valid():
            # Capturamos las variables que llegan por POST
            usuario = request.POST['usuario']
            clave = request.POST['clave']
            auth.login(request, validator.acceso)  # Crear una sesion
            return HttpResponseRedirect('informeusu')

        else:
            return render_to_response('login.html', {'error': validator.getMessage()},
                                      context_instance=RequestContext(request))

    return render_to_response('login.html', context_instance=RequestContext(request))


def informeusu(request):
    return render(request, 'informeusu.html')


def registroben(request):
    departamentos = Departamento.objects.all()
    ciudades = Ciudad.objects.all()
    return render_to_response('registroben.html',
                              {'departamentos': departamentos, 'ciudades': ciudades, 'listaEscolar': ListaEscolaridad,
                               'estrato': ListaEstrato, 'genero': ListaGenero})


def informeben(request):
    return render(request, 'informeben.html')


from django.db.models import Q


def search(request):
    """view de los resultados de busqueda
    """
    cursos = None
    filter = None
    if 'filter' in request.GET.keys():
        filter = request.GET['filter']
        qset = (Q(name__icontains=filter) |
                Q(price__icontains=filter) |
                Q(teacher__name__icontains=filter)
                )
        cursos = Course.objects.filter(qset)

        """
        Manera de realizar consultar por un criterio a la vez
        #buscamos por nombre del curso
        cursos = Course.objects.filter( name__icontains =  request.GET['filter'] )
        # Si no existen resultados buscarmos por precio
        if not cursos.exists():
            cursos = Course.objects.filter( price__icontains =  request.GET['filter'] )
        # Si no existen resultados buscarmos por profesor
        if not cursos.exists():
            cursos = Course.objects.filter( teacher__name__icontains =  request.GET['filter'] )
        filter = request.GET['filter']
        """

    return render_to_response('index.html', {'cursos': cursos, 'filtro': filter},
                              context_instance=RequestContext(request))


from django.core import serializers
from django.http import HttpResponse


def registrobenAjax(request, *args, **kwargs):
    id_departamento = request.GET['id']
    ciudad = Ciudad.objects.filter(departamento__id=id_departamento)
    data = serializers.serialize('json', ciudad,
                                 fields=('ciudad'))
    return render_to_response(data, mimetype='application/json')
