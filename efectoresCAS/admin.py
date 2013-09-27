import autocomplete_light
autocomplete_light.autodiscover()
from django.contrib import admin
admin.autodiscover()
from efectoresCAS.models import *
from django.http import HttpResponseRedirect
from django.utils.encoding import force_unicode
from django.utils.translation import ugettext_lazy as _




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

class EfectoresAreaInline(admin.TabularInline):
    model = efector_codigoporarea
    form = autocomplete_light.modelform_factory(efector)
    raw_id_fields = ['efector',]


class DescInLine(admin.TabularInline):
    model = descripcion


class ConceptAdmin(admin.ModelAdmin):
    list_filter = ['revisado',]
    list_display = ['fsn','revisado']
    inlines = DescInLine,ConceptosAreaInline
    actions = [export_as_csv]
    search_fields = ['fsn',]
    def add_view(self, request, *args, **kwargs):
        result = super(ConceptAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result

    def change_view(self, request, object_id, form_url='', extra_context=None):

        result = super(ConceptAdmin, self).change_view(request, object_id, form_url, extra_context )

        ref = request.META.get('HTTP_REFERER', '')
        if ref.find('?') != -1:
            request.session['filtered'] =  ref

        if request.POST.has_key('_save'):
            try:
                if request.session['filtered'] is not None:
                    result['Location'] = request.session['filtered']
                    request.session['filtered'] = None
            except:
                pass

        return result
    def response_change(self, request, obj):
        """
        Determines the HttpResponse for the change_view stage.
        """
        if request.POST.has_key("_viewnext"):
            msg = (_('The %(name)s "%(obj)s" was changed successfully.') %
                   {'name': force_unicode(obj._meta.verbose_name),
                    'obj': force_unicode(obj)})
            next = obj.__class__.objects.filter(id__gt=obj.id).order_by('id')[:1]
            if next:
                self.message_user(request, msg)
                return HttpResponseRedirect("../%s/" % next[0].pk)
        return super(ConceptAdmin, self).response_change(request, obj)
admin.site.register(concepto,ConceptAdmin)


class efectorAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(efector)
    list_display = ['ExamCode','ExamName','get_conceptosporarea']
    filter_vertical = ('codigoporarea',)
    search_fields = ['ExamCode','ExamName']
    actions = [export_as_csv]
admin.site.register(efector,efectorAdmin)


class descripcionAdmin(admin.ModelAdmin):
    list_display = ['termino','tipodescripcion','id_concepto']
    list_filter = ['tipodescripcion']
    search_fields = ['termino',]
    actions = [export_as_csv]
admin.site.register(descripcion,descripcionAdmin)


class efectorareaAdmin(admin.ModelAdmin):
    list_display = ('id','efector','conceptoscasporarea')
    ordering = ('id',)
    raw_id_fields = ('conceptoscasporarea',)
    search_fields = ('efector__ExamName',)
admin.site.register(efector_codigoporarea,efectorareaAdmin)


class concCasAreaAdmin(admin.ModelAdmin):
    inlines = EfectoresAreaInline,
    list_display = ['concepto','area','get_efectorxarea']
    list_filter = ['area']
admin.site.register(conceptosCASporarea,concCasAreaAdmin)

admin.site.register(cas_area)
admin.site.register(cas_lugar)

__author__ = 'ehebel'
