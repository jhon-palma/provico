# -*- encoding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib import auth
from django.conf import settings
from .models import Usuario
from django.http import HttpResponseRedirect, HttpResponseBadRequest, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.core.exceptions import NON_FIELD_ERRORS
from app.models import Departamento
from app.models import Ciudad
from app.models import ListaEscolaridad
from app.models import ListaEstrato
from app.models import ListaGenero
from app.models import ListaTipoDocumento
from app.models import Beneficiario
from validators import FormContacto,FormRegistroValidator, FormLoginValidator
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.template.loader import render_to_string
# Create your views here.

def index(request):
    
    #return render(request, 'landing.html')

    if request.method == 'POST':
        validator = FormContacto(request.POST)
        validator.required = ['name', 'email', 'telefono', 'asunto', 'mensaje']

        if validator.is_valid():
            htmly = get_template('mail.html')

            name = request.POST['name']
            from_email = request.POST['email']
            telefono = request.POST['telefono']
            asunto = request.POST['asunto']
            ast = "Dudas o inquietud ProViCo"
            mensaje = request.POST['mensaje']
            body = render_to_string('mail.html',{'name':name,'asunto':asunto,'from_email':from_email,'telefono':telefono, 'mensaje':mensaje})
            #contexto = Context({name})
            #html_content = htmly.render(contexto)

            msg = EmailMultiAlternatives(ast, body , from_email ,  [ settings.EMAIL_HOST_USER])
            #msg.attach_alternative(html_content, "text/html")
            #msg.send()
            msg.content_subtype = "html"
            msg.send()

            #send_mail(asunto, body, from_email ,  [ settings.EMAIL_HOST_USER] )
            return render_to_response('landing.html', {'success': True, 'error':validator.getMessage()}, context_instance = RequestContext(request))
        else:
            return render_to_response('landing.html', {'error': validator.getMessage()}, context_instance=RequestContext(request))
    return render_to_response('landing.html',  context_instance=RequestContext(request))

from django.contrib.auth.hashers import make_password
	

def registrousu(request):
    error = False

    if request.method == 'POST':

        validator = FormRegistroValidator(request.POST)
        validator.required = ['nombre', 'apellidos', 'cedula', 'email', 'password', 'perfil']

        if validator.is_valid():
            usuario = User()
            usuario.first_name = request.POST['nombre']
            usuario.last_name = request.POST['apellidos']
            usuario.username = request.POST['cedula']
            usuario.email = request.POST['email']
            usuario.password = make_password(request.POST['password'])
            tipo = request.POST['perfil']
            #TODO: ENviar correo electronico para confirmar cuenta
            usuario.is_active = True
            perfil = Group.objects.get(id = tipo)
            usuario.save()
            usuario.groups.add(perfil)
            usuario.save()
            return render_to_response('registrousu.html', {'success': True}, context_instance=RequestContext(request))
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
            return HttpResponseRedirect('principal')

        else:
            return render_to_response('home.html', {'error': validator.getMessage()},
                                      context_instance=RequestContext(request))

    return render_to_response('home.html', context_instance=RequestContext(request))


def informeusu(request):
    return render(request, 'informeusu.html')

#@login_required(login_url="/login") # Protegemos la vista con el decorador del loguin para que solo pueda ingresar un usuario logueado
def registroben(request):
    error = False
    departamentos = Departamento.objects.all()
    ciudades = Ciudad.objects.all()

    InfoFormulario= {'departamentos': departamentos, 'ciudades': ciudades, 'listaEscolar': ListaEscolaridad, 'tipoDocumento':ListaTipoDocumento,
                               'estrato': ListaEstrato, 'genero': ListaGenero}

    if request.method == 'POST':
        validator = FormRegistroValidator(request.POST)
        validator.required = ['nombre', 'apellido', 'cedula', 'email', 'telefono', 'direccion']

        if request.method == 'POST':
            beneficiario = Beneficiario()
            # Capturamos las variables que llegan por POST
            beneficiario.nombre = request.POST['nombre']
            beneficiario.apellido = request.POST['apellido']
            beneficiario.numeroDocumento = request.POST['numeroDocumento']
            beneficiario.genero = request.POST['genero']
            #beneficiario.nace = request.POST['date'] formato ojo manda diamesaño recibe añomesdia
            beneficiario.email = request.POST['email']
            beneficiario.telefono = request.POST['telefono']
            beneficiario.direccion = request.POST['direccion']
            beneficiario.estrato = request.POST["estrato"]
            beneficiario.escolaridad = request.POST["educacion"]
            beneficiario.ocupacion = request.POST["ocupacion"]
            beneficiario.parentesco = request.POST["parentesco"]
            beneficiario.cabeza = request.POST["cedulacabeza"]
            beneficiario.ciudad_id =  request.POST["ciudad"]
            beneficiario.save()
            InfoFormulario.update({'success': True})
            return render_to_response('registroben.html', InfoFormulario , context_instance=RequestContext(request))
        else:
            InfoFormulario.update({'error': validator.getMessage()})
            return render_to_response('registroben.html',InfoFormulario , context_instance=RequestContext(request))
    else:
        return render_to_response('registroben.html', InfoFormulario, context_instance=RequestContext(request))


def informeben(request):
    return render(request, 'informeben.html')

def landing(request):
    return render(request, 'landing.html')

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

    return render_to_response('principal.html', {'cursos': cursos, 'filtro': filter},
                              context_instance=RequestContext(request))


from django.core import serializers
from django.http import HttpResponse


def registrobenAjax(request):
    id_departamento = request.GET['id']
    ciudad = Ciudad.objects.filter(departamento__id=id_departamento)
    data = serializers.serialize('json', ciudad, fields=('ciudad','codigo'))
    return HttpResponse(data, content_type='application/json')

def principal(request):
    return render(request, 'principal.html')

@login_required(login_url="/login") # Protegemos la vista con el decorador del loguin para que solo pueda ingresar un usuario logueado
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/login")
