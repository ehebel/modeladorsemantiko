import autocomplete_light
autocomplete_light.autodiscover()
from privilegiosCAS.models import *
from django.contrib import admin
from django.forms import TextInput
from autocomplete_light.forms import FixedModelForm

ModelForm = FixedModelForm


admin.site.register(especialidad)
admin.site.register(area)

#TODO: Agregar descarga como CSV y visualizacion de todas las tablas de relacion

class amcaAdmin(admin.ModelAdmin):
    search_fields = ['amca_desc',]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})}}
    #   fields = ['amca_cod','amca_desc','homologadocas']
    list_display = ['amca_cod','amca_desc','homologadocas']
    radio_fields = {
        "homologadocas": admin.HORIZONTAL}
admin.site.register(amca,amcaAdmin)

class intervAdmin(admin.ModelAdmin):
    search_fields = ['interv_glosa',]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})}}
    list_display = ['id_intev','interv_glosa','grpdescripcion','sgrdescripcion','amca_cod']
admin.site.register(intervencion,intervAdmin)

admin.site.register(tipo_privilegio)

class privilAdmin(admin.ModelAdmin):
    search_fields = ['descripcion',]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})}}
    form = autocomplete_light.modelform_factory(privilegio)
    list_display = ['descripcion','get_area','get_amca', 'get_']
admin.site.register(privilegio,privilAdmin)

admin.site.register(tipo_documento)
admin.site.register(documento)
admin.site.register(atributo)



__author__ = 'ehebel'
