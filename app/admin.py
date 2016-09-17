from django.contrib import admin
from app.models import Departamento, Ciudad

# Register your models here.

class CiudadChildrenAdmin(admin.TabularInline):
    model = Ciudad


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    inlines = (CiudadChildrenAdmin ,)


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ('ciudad','departamento_id',)
    search_fields = ('ciudad', 'departamento_id__departamento')
