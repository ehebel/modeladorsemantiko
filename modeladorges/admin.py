import autocomplete_light
autocomplete_light.autodiscover()

from django.contrib import admin
admin.autodiscover()
from django.forms import TextInput, Textarea
from modeladorges.models import *
import csv
from django.http import HttpResponse
from django.core.exceptions import PermissionDenied


def export_as_csv(modeladmin, request, queryset):
    """
    Generic csv export admin action.
    """
    if not request.user.is_staff:
        raise PermissionDenied
    opts = modeladmin.model._meta
    response = HttpResponse(mimetype='text/csv')
    response['Content-Disposition'] = 'attachment; filename=%s.csv' % unicode(opts).replace('.', '_')
    writer = csv.writer(response, delimiter=';')
    field_names = [field.name for field in opts.fields]
    # Write a first row with header information
    writer.writerow(field_names)
    # Write data rows
    for obj in queryset:
        values = []
        for field in field_names:
            value = (getattr(obj, field))
            if callable(value):
                try:
                    value = value() or ''
                except:
                    value = 'Error retrieving value'
            if value is None:
                value = ''
            values.append(unicode(value).encode('utf-8'))
        writer.writerow(values)
        #writer.writerow([getattr(obj, field) for field in field_names])
    return response
export_as_csv.short_description = "Exportar elementos seleccionados como CSV"

class GesAdmin(admin.ModelAdmin):
    search_fields = ['glosa',]
    list_display = ['id','glosa','get_cie']
    form = autocomplete_light.modelform_factory(ges_patologia)
    actions = [export_as_csv]
admin.site.register(ges_patologia, GesAdmin)


class DescInLine(admin.TabularInline):
    model = descripcione
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        #models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

class DescAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(descripcione)
    ordering = ['termino']
admin.site.register(descripcione, DescAdmin)


class ConceptAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(concepto)
    inlines = DescInLine,
admin.site.register(concepto,ConceptAdmin)


class cieDeisAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(ciediez)
admin.site.register(ciediez,cieDeisAdmin)

class casProcedAdmin(admin.ModelAdmin):
    list_display = ['idintervencionclinica','integlosa','grpdescripcion']
    list_filter = ['grpdescripcion','sgrdescripcion']
admin.site.register(casprocedimiento,casProcedAdmin)


admin.site.register(casdiagnostico)



__author__ = 'ehebel'