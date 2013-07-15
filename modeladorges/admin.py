import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()

from modeladorges.models import ciediez,casdiagnostico,casprocedimiento,ges_patologia


class GesAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(ges_patologia)
admin.site.register(ges_patologia, GesAdmin)

#admin.site.register(ges_patologia)
admin.site.register(ciediez)
admin.site.register(casprocedimiento)
admin.site.register(casdiagnostico)


__author__ = 'ehebel'