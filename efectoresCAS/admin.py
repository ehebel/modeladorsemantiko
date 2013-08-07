from django.contrib import admin
from efectoresCAS.models import *

admin.site.register(descripcion)
admin.site.register(concepto)
admin.site.register(cas_areas)
admin.site.register(cas_lugares)
admin.site.register(radiologico)
admin.site.register(conceptosCASporarea)

__author__ = 'ehebel'
