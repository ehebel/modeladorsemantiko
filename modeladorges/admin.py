import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()
from django.forms import TextInput, Textarea
from modeladorges.models import *


class GesAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(ges_patologia)
admin.site.register(ges_patologia, GesAdmin)


class DescInLine(admin.TabularInline):
    model = descripcione
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        #models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

class DescAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(descripcione)
admin.site.register(descripcione, DescAdmin)


class ConceptAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(concepto)
    inlines = DescInLine,
admin.site.register(concepto,ConceptAdmin)


admin.site.register(ciediez)
admin.site.register(casprocedimiento)
admin.site.register(casdiagnostico)



__author__ = 'ehebel'