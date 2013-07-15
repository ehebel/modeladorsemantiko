import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

from modeladorges.models import *


class GesAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(ges_patologia)
admin.site.register(ges_patologia, GesAdmin)

#admin.site.register(ges_patologia)
admin.site.register(ciediez)
admin.site.register(casprocedimiento)
admin.site.register(casdiagnostico)
admin.site.register(concepto)
admin.site.register(descripcione)


__author__ = 'ehebel'