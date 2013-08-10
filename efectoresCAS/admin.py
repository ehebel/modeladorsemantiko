from django.contrib import admin
from efectoresCAS.models import *


class DescInLine(admin.TabularInline):
    model = descripcion


class ConceptAdmin(admin.ModelAdmin):
    inlines = DescInLine,


admin.site.register(descripcion)
admin.site.register(concepto,ConceptAdmin)
admin.site.register(cas_area)
admin.site.register(cas_lugar)
admin.site.register(efector)
admin.site.register(conceptosCASporarea)

__author__ = 'ehebel'
