from django.contrib import admin
admin.autodiscover()
from efectoresCAS.models import *


import autocomplete_light
autocomplete_light.autodiscover()


class DescInLine(admin.TabularInline):
    model = descripcion


class ConceptAdmin(admin.ModelAdmin):
    inlines = DescInLine,


class efectorAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(efector)
    #filter_vertical = ('codigoporarea',)


admin.site.register(descripcion)
admin.site.register(concepto,ConceptAdmin)
admin.site.register(cas_area)
admin.site.register(cas_lugar)
admin.site.register(efector,efectorAdmin)
admin.site.register(conceptosCASporarea)

__author__ = 'ehebel'
