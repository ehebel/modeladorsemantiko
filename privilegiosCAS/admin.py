import autocomplete_light
autocomplete_light.autodiscover()
from privilegiosCAS.models import *
from django.contrib import admin
from django.forms import TextInput

admin.site.register(especialidad)
admin.site.register(area)

class amcaAdmin(admin.ModelAdmin):
    list_display = ['amca_cod','amca_desc','homologadocas']
    radio_fields = {
        "homologadocas": admin.HORIZONTAL}
admin.site.register(amca)

class intervAdmin(admin.ModelAdmin):
    list_display = ['id_intev','interv_glosa','grpdescripcion','sgrdescripcion','amca_cod']
admin.site.register(intervencion,intervAdmin)

admin.site.register(tipo_privilegio)

class privilAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})}}
    form = autocomplete_light.modelform_factory(privilegio)
admin.site.register(privilegio,privilAdmin)

admin.site.register(tipo_documento)
admin.site.register(documento)
admin.site.register(atributo)



__author__ = 'ehebel'
