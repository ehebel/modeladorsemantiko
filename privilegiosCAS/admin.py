import autocomplete_light
autocomplete_light.autodiscover()
import csv
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import FieldListFilter
from django.utils.encoding import force_unicode

from privilegiosCAS.models import *
from django.contrib import admin
from django.forms import TextInput
from autocomplete_light.forms import FixedModelForm
from django.contrib.admin import SimpleListFilter
ModelForm = FixedModelForm




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


class AMCAFilter(SimpleListFilter):
    title = 'Codigos AMCA' # or use _('country') for translated title
    parameter_name = 'amca_cod'

    def lookups(self, request, model_admin):
        amcas = set([c.amca_cod for c in model_admin.model.objects.all()])
        return [(c.amca_cod, c.amca_desc) for c in amcas]

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(amca_cod__amca_cod__exact=self.value())
        else:
            return queryset

class especialidadAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
admin.site.register(especialidad,especialidadAdmin)

class areaAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
admin.site.register(area,areaAdmin)


#TODO: Agregar descarga como CSV y visualizacion de todas las tablas de relacion

class amcaAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
    search_fields = ['amca_desc',]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})}}
    list_display = ['amca_cod','amca_desc','homologadocas']
    radio_fields = {
        "homologadocas": admin.HORIZONTAL}
admin.site.register(amca,amcaAdmin)

class intervAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
    list_filter = ['grpdescripcion','sgrdescripcion','amca_cod__amca_desc']
    #list_filter = [AMCAFilter,]
    form = autocomplete_light.modelform_factory(intervencion)
    search_fields = ['interv_glosa','amca_cod__amca_cod','amca_cod__amca_desc']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})}}
    list_display = ['id_intev','interv_glosa','grpdescripcion','sgrdescripcion','amca_cod']
admin.site.register(intervencion,intervAdmin)

admin.site.register(tipo_privilegio)

class privilAdmin(admin.ModelAdmin):
    actions = [export_as_csv]
    search_fields = ['descripcion',]
    list_filter = ['seleccionado','rel_area','rel_especialidad']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})}}
    form = autocomplete_light.modelform_factory(privilegio)
    list_display = ['descripcion','get_area','get_amca','get_especialidad',]


    def add_view(self, request, *args, **kwargs):
        result = super(privilAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result

    def change_view(self, request, object_id, form_url='', extra_context=None):

        result = super(privilAdmin, self).change_view(request, object_id, form_url, extra_context )

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
            next = obj.__class__.objects.filter(id_xt_mc__gt=obj.id_xt_mc).order_by('id_xt_mc')[:1]
            if next:
                self.message_user(request, msg)
                return HttpResponseRedirect("../%s/" % next[0].pk)
        return super(privilAdmin, self).response_change(request, obj)
    def save_model(self, request, obj, form, change):

        if not hasattr(obj, 'usuario_creador'):
            obj.usuario_creador = request.user
        obj.save()

        instance = form.save(commit=False)
        if not hasattr(instance,'usuario_ult_mod'):
            instance.usuario_ult_mod = request.user
        instance.usuario_ult_mod = request.user
        instance.save()
        form.save_m2m()
        return instance

    def save_formset(self, request, form, formset, change):
        def set_user(instance):
            if not instance.usuario_ult_mod:
                instance.usuario_ult_mod = request.user
            instance.usuario_ult_mod = request.user
            instance.save()
        if formset.model == privilegio:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()


admin.site.register(privilegio,privilAdmin)



admin.site.register(tipo_documento)
admin.site.register(documento)
admin.site.register(atributo)

class relAdmin (admin.ModelAdmin):
    actions = [export_as_csv]




__author__ = 'ehebel'
