from django.contrib import admin
from efectoresCAS.models import *


class DescInLine(admin.TabularInline):
    model = descripcion


class ConceptAdmin(admin.ModelAdmin):
    inlines = DescInLine,


admin.site.register(descripcion)
admin.site.register(concepto,ConceptAdmin)
admin.site.register(cas_areas)
admin.site.register(cas_lugares)
admin.site.register(efector)
admin.site.register(conceptosCASporarea)

__author__ = 'ehebel'
