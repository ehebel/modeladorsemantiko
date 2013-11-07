import autocomplete_light
autocomplete_light.autodiscover()
from privilegiosCAS.models import *
from django.contrib import admin
from django.forms import TextInput
from autocomplete_light.forms import FixedModelForm
from django.contrib.admin import SimpleListFilter
ModelForm = FixedModelForm


class AMCAFilter(SimpleListFilter):
    title = 'Codigos AMCA' # or use _('country') for translated title
    parameter_name = 'amca_cod'

    def lookups(self, request, model_admin):
        amcas = set([c.amca_cod for c in model_admin.model.objects.all()])
        return [(c.amca_cod, c.amca_desc) for c in amcas]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(amca_cod__amca_cod__exact=self.value())
        else:
            return queryset

admin.site.register(especialidad)
admin.site.register(area)

#TODO: Agregar descarga como CSV y visualizacion de todas las tablas de relacion

class amcaAdmin(admin.ModelAdmin):
    search_fields = ['amca_desc',]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})}}
    list_display = ['amca_cod','amca_desc','homologadocas']
    radio_fields = {
        "homologadocas": admin.HORIZONTAL}
admin.site.register(amca,amcaAdmin)

class intervAdmin(admin.ModelAdmin):
    list_filter = ['grpdescripcion','sgrdescripcion','amca_cod__amca_desc']
    #list_filter = [AMCAFilter,]
    form = autocomplete_light.modelform_factory(intervencion)
    search_fields = ['interv_glosa','amca_cod__amca_cod','amca_cod__amca_desc']
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
    list_display = ['descripcion','get_area','get_amca','get_especialidad',]
admin.site.register(privilegio,privilAdmin)

admin.site.register(tipo_documento)
admin.site.register(documento)
admin.site.register(atributo)



__author__ = 'ehebel'
