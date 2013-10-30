import autocomplete_light
autocomplete_light.autodiscover()
from privilegiosCAS.models import *
from django.contrib import admin

admin.site.register(especialidad)
admin.site.register(area)
admin.site.register(amca)
admin.site.register(intervencion)
admin.site.register(tipo_privilegio)

class privilAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(privilegio)

admin.site.register(privilegio,privilAdmin)
admin.site.register(tipo_documento)
admin.site.register(documento)
admin.site.register(atributo)



__author__ = 'ehebel'
