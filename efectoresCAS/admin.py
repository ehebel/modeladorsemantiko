from django.contrib import admin
admin.autodiscover()
from efectoresCAS.models import *




import autocomplete_light
autocomplete_light.autodiscover()

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

class ConceptosAreaInline(admin.TabularInline):
    model = cas_area.conceptosporarea.through


class DescInLine(admin.TabularInline):
    model = descripcion


class ConceptAdmin(admin.ModelAdmin):
    list_filter = ['revisado',]
    inlines = DescInLine,ConceptosAreaInline
    actions = [export_as_csv]


class efectorAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(efector)
    filter_vertical = ('codigoporarea',)
    actions = [export_as_csv]


class descripcionAdmin(admin.ModelAdmin):
    list_display = ['descripcion','tipodescripcion','id_concepto']
    list_filter = ['tipodescripcion']
    actions = [export_as_csv]




admin.site.register(descripcion)
admin.site.register(concepto,ConceptAdmin)
admin.site.register(cas_area)
admin.site.register(cas_lugar)
admin.site.register(efector,efectorAdmin)
admin.site.register(conceptosCASporarea)

__author__ = 'ehebel'
