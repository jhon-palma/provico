from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Usuario(User):
    class Meta:
        proxy = True

class Departamento(models.Model):
    codigo = models.CharField(max_length=2)
    departamento = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos'

    def __unicode__(self):
        return self.departamento

class Ciudad(models.Model):
    codigo = models.CharField(max_length=3)
    ciudad = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __unicode__(self):
        return self.ciudad


ListaEscolaridad = (
    ("Pr", 'Primaria'),
    ("Sc", 'Secundaria'),
    ("Te", 'Tecnico'),
    ("Tl", 'Tecnologo'),
    ("Pr", 'Profesional'),
    ("NR", 'No registra'),
)

ListaEstrato = (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)

ListaGenero = (
    ('M','M'),
    ('F','F'),
)

ListaTipoDocumento = (
    ('RC','RC'),
    ('TI','TI'),
    ('CC','CC'),
    ('CE','CE'),
)
ListaParentezco = (
    ('Hijo', )
)
class Beneficiario(models.Model):
    tipoDocumento = models.CharField(max_length=2, choices=ListaTipoDocumento)
    numeroDocumento = models.IntegerField()
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    ciudad = models.ForeignKey(Ciudad)
    genero = models.CharField(max_length=1, choices=ListaGenero)
    nace = models.DateField(null=True)
    email = models.EmailField()
    telefono = models.IntegerField()
    direccion = models.CharField(max_length=50)
    estrato = models.IntegerField(choices=ListaEstrato)
    escolaridad = models.CharField(max_length=2, choices=ListaEscolaridad)
    ocupacion = models.CharField(max_length=50)
    parentesco = models.CharField(max_length=50)
    cabeza = models.IntegerField()

