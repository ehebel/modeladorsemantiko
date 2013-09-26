import autocomplete_light
autocomplete_light.autodiscover()
from django.forms import TextInput, Textarea
from django.contrib import admin
admin.autodiscover()
from modeladorFarmacos.models import *
import csv
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from django.contrib.admin import FieldListFilter
from django.utils.encoding import force_unicode


class IsNullFieldListFilter(FieldListFilter):
    def __init__(self, field, request, params, model, model_admin, field_path):
        self.lookup_kwarg = '%s__isnull' % field_path
        self.lookup_val = request.GET.get(self.lookup_kwarg, None)
        super(IsNullFieldListFilter, self).__init__(field,
            request, params, model, model_admin, field_path)

    def expected_parameters(self):
        return [self.lookup_kwarg]

    def choices(self, cl):
        for lookup, title in (
            (None, _('All')),
            ('False', _('Con Elementos')),
            ('True', _('Sin Elementos'))):
            yield {
                'selected': self.lookup_val == lookup,
                'query_string': cl.get_query_string({
                    self.lookup_kwarg: lookup,
                    }),
                'display': title,
                }

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

class ProductoComercialInline(admin.TabularInline):
    model = xt_pc
    form = autocomplete_light.modelform_factory(xt_pc)

class SustanciaClinicoInline(admin.TabularInline):
    model = xt_mc.rel_mc.through
    form = autocomplete_light.modelform_factory(rel_mc_sust)
    radio_fields = {
        "estado": admin.HORIZONTAL}

class SustanciaBasicoInline(admin.TabularInline):
    model = xt_mb.rel_xt_sust.through
    form = autocomplete_light.modelform_factory(rel_xt_mb_xt_sust)
    radio_fields = {
        "estado": admin.HORIZONTAL}

class bioeqAdminInline(admin.TabularInline):
    model = xt_bioequivalente
    form = autocomplete_light.modelform_factory(xt_bioequivalente)
    fk_name = 'referencia'

#Inicia ADMIN de modelos Completos
#Para mejorar facilidad de busqueda

class xt_sustanciasAdmin (admin.ModelAdmin):
    list_display = ['id_xt_sust','descripcion','riesgo_teratogenico','concept_sust_dmd']
    list_filter = ['revisado','consultar','estado']
    search_fields = ['descripcion',]
    ordering = ['descripcion',]
    def add_view(self, request, *args, **kwargs):
        result = super(xt_sustanciasAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result

    def change_view(self, request, object_id, form_url='', extra_context=None):

        result = super(xt_sustanciasAdmin, self).change_view(request, object_id, form_url, extra_context )

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
            next = obj.__class__.objects.filter(id_xt_sust__gt=obj.id_xt_sust).order_by('id_xt_sust')[:1]
            if next:
                self.message_user(request, msg)
                return HttpResponseRedirect("../%s/" % next[0].pk)
        return super(xt_sustanciasAdmin, self).response_change(request, obj)

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
        if formset.model == xt_mc:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()
admin.site.register(xt_sustancias,xt_sustanciasAdmin)

class mcAdmin (admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})}
    }
    form = autocomplete_light.modelform_factory(xt_mc)
    inlines = [SustanciaClinicoInline] # ,ProductoComercialInline]
    search_fields = ['descripcion']
    list_display = ['id_xt_mc','descripcion','med_basico','get_sustancia','get_pc'
        ,'estado_prescripcion','tipo_forma_farm','concept_vmp_dmd']
    list_filter = ['revisado','consultar','estado'
        ,('med_basico', IsNullFieldListFilter)
        ,('concept_vmp_dmd', IsNullFieldListFilter)
        ] #TODO con/sin observacion
    list_display_links = ['id_xt_mc','descripcion']
    actions = [export_as_csv]
    readonly_fields=('id_xt_mc',)

    radio_fields = {
                "estado": admin.HORIZONTAL
                ,"consultar": admin.HORIZONTAL
                ,"revisado": admin.HORIZONTAL
                ,"tipo_forma_farm": admin.HORIZONTAL
    }
    def add_view(self, request, *args, **kwargs):
        result = super(mcAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result
    def change_view(self, request, object_id, form_url='', extra_context=None):

        result = super(mcAdmin, self).change_view(request, object_id, form_url, extra_context )

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
        return super(mcAdmin, self).response_change(request, obj)
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
        if formset.model == xt_mc:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()
admin.site.register(xt_mc,  mcAdmin)

class mbAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})}}
    form = autocomplete_light.modelform_factory(xt_mb)
    inlines = [SustanciaBasicoInline,]
    ordering = ['descripcion',]
    search_fields = ['descripcion']
    list_display = ['xt_id_mb','descripcion','get_sustancia','concept_vtm_hiba','kairos_sustancia','concept_vtm_dmd']
    list_filter = ['revisado','consultar','estado'
        ,('concept_vtm_dmd', IsNullFieldListFilter)]
    list_display_links = ['xt_id_mb','descripcion']
    actions = [export_as_csv]
    readonly_fields=('xt_id_mb',)

    radio_fields = {
        "estado": admin.HORIZONTAL
        ,"consultar": admin.HORIZONTAL
        ,"revisado": admin.HORIZONTAL
    }
    def add_view(self, request, *args, **kwargs):
        result = super(mbAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result

    def change_view(self, request, object_id, form_url='', extra_context=None):

        result = super(mbAdmin, self).change_view(request, object_id, form_url, extra_context )

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
            next = obj.__class__.objects.filter(xt_id_mb__gt=obj.xt_id_mb).order_by('xt_id_mb')[:1]
            if next:
                self.message_user(request, msg)
                return HttpResponseRedirect("../%s/" % next[0].pk)
        return super(mbAdmin, self).response_change(request, obj)
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
        if formset.model == xt_mc:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()
admin.site.register(xt_mb,  mbAdmin)

class mcceAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(xt_mcce)
    list_display = ['id_xt_mcce','descripcion','id_xt_mc','concept_vmpp_dmd'] #TODO sustancias m2m
    list_filter = ['revisado','consultar','estado',('concept_vmpp_dmd', IsNullFieldListFilter)] #TODO con/Sin observacion
    search_fields = ['descripcion',]
    readonly_fields=('id_xt_mcce',)
    radio_fields = {
        "estado": admin.HORIZONTAL
        ,"consultar": admin.HORIZONTAL
        ,"revisado": admin.HORIZONTAL
    }
    def add_view(self, request, *args, **kwargs):
        result = super(mcceAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result
    def change_view(self, request, object_id, form_url='', extra_context=None):

        result = super(mcceAdmin, self).change_view(request, object_id, form_url, extra_context )

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
            next = obj.__class__.objects.filter(id_xt_mcce__gt=obj.id_xt_mcce).order_by('id_xt_mcce')[:1]
            if next:
                self.message_user(request, msg)
                return HttpResponseRedirect("../%s/" % next[0].pk)
        return super(mcceAdmin, self).response_change(request, obj)
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
        if formset.model == xt_mc:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()

admin.site.register(xt_mcce,mcceAdmin)

class pcAdmin(admin.ModelAdmin):
    inlines = [bioeqAdminInline,]
    search_fields = ['descripcion',]
    list_display = ['id_xt_pc','descripcion','id_xt_fp','id_xt_mc','concept_amp_dmd'] #TODO BOOL Bioequivalente
    list_filter = ['estado','revisado','consultar'
        ,('id_xt_mc', IsNullFieldListFilter)
        ,('concept_amp_dmd', IsNullFieldListFilter)
    ] #TODO BOOL Observacion
    form = autocomplete_light.modelform_factory(xt_pc)
    readonly_fields=('id_xt_pc',)
    radio_fields = {
        "estado": admin.HORIZONTAL
        ,"consultar": admin.HORIZONTAL
        ,"revisado": admin.HORIZONTAL
    }
    def add_view(self, request, *args, **kwargs):
        result = super(pcAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result

    def change_view(self, request, object_id, form_url='', extra_context=None):

        result = super(pcAdmin, self).change_view(request, object_id, form_url, extra_context )

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
            next = obj.__class__.objects.filter(id_xt_pc__gt=obj.id_xt_pc).order_by('id_xt_pc')[:1]
            if next:
                self.message_user(request, msg)
                return HttpResponseRedirect("../%s/" % next[0].pk)
        return super(pcAdmin, self).response_change(request, obj)

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
        if formset.model == xt_mc:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()
admin.site.register(xt_pc,  pcAdmin)

class pcceAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(xt_pcce)
    list_filter = ['estado','revisado','consultar'
        ,('id_xt_mcce', IsNullFieldListFilter)] #TODO BOOL Observacion
    list_display = ['id_xt_pcce','descripcion','id_xt_pc','id_xt_mcce','concept_ampp_dmd','id_presentacion_kairos'] #TODO BOOL Bioequivalente
    search_fields = ['descripcion',]
    readonly_fields=('id_xt_pcce',)
    radio_fields = {
        "estado": admin.HORIZONTAL
        ,"consultar": admin.HORIZONTAL
        ,"revisado": admin.HORIZONTAL
    }
    def add_view(self, request, *args, **kwargs):
        result = super(pcceAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result

    def change_view(self, request, object_id, form_url='', extra_context=None):

        result = super(pcceAdmin, self).change_view(request, object_id, form_url, extra_context )

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
            next = obj.__class__.objects.filter(id_xt_pcce__gt=obj.id_xt_pcce).order_by('id_xt_pcce')[:1]
            if next:
                self.message_user(request, msg)
                return HttpResponseRedirect("../%s/" % next[0].pk)
        return super(pcceAdmin, self).response_change(request, obj)

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
        if formset.model == xt_mc:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()
admin.site.register(xt_pcce,pcceAdmin)

class xtlabAdmin(admin.ModelAdmin):
    list_display = ['id_xt_lab','descripcion','clave_lab_kairos']
    list_filter = ['revisado','consultar','estado',('clave_lab_kairos', IsNullFieldListFilter)]
    search_fields = ['descripcion',]
    def response_change(self, request, obj):
        """
        Determines the HttpResponse for the change_view stage.
        """
        if request.POST.has_key("_viewnext"):
            msg = (_('The %(name)s "%(obj)s" was changed successfully.') %
                   {'name': force_unicode(obj._meta.verbose_name),
                    'obj': force_unicode(obj)})
            next = obj.__class__.objects.filter(id_xt_lab__gt=obj.id_xt_lab).order_by('id_xt_lab')[:1]
            if next:
                self.message_user(request, msg)
                return HttpResponseRedirect("../%s/" % next[0].pk)
        return super(xtlabAdmin, self).response_change(request, obj)

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
        if formset.model == xt_mc:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()

    def add_view(self, request, *args, **kwargs):
        result = super(xtlabAdmin, self).add_view(request, *args, **kwargs )
        request.session['filtered'] =  None
        return result

    def change_view(self, request, object_id, form_url='', extra_context=None):

        result = super(xtlabAdmin, self).change_view(request, object_id, form_url, extra_context )

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
admin.site.register(xt_laboratorio,xtlabAdmin)

class uduAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):

        if not hasattr(obj, 'usuario_creador'):
            obj.usuario_creador = request.user
        obj.save()
admin.site.register(xt_unidad_dosis_unitaria,uduAdmin)

class umuAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):

        if not hasattr(obj, 'usuario_creador'):
            obj.usuario_creador = request.user
        obj.save()
admin.site.register(xt_unidad_medida_unitaria,uduAdmin)

class ffAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):

        if not hasattr(obj, 'usuario_creador'):
            obj.usuario_creador = request.user
        obj.save()
admin.site.register(xt_formas_farm,ffAdmin)

class condVentaAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):

        if not hasattr(obj, 'usuario_creador'):
            obj.usuario_creador = request.user
        obj.save()
admin.site.register(xt_condicion_venta,condVentaAdmin)


admin.site.register(xt_unidad_potencia)


class gfpAdmin(admin.ModelAdmin):
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
        if formset.model == xt_mc:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()
admin.site.register(xt_gfp,gfpAdmin)

class fpAdmin(admin.ModelAdmin):
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
        if formset.model == xt_mc:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()
admin.site.register(xt_fp,fpAdmin)

class productoAdmin(admin.ModelAdmin):
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
        if formset.model == xt_mc:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()
admin.site.register(xt_producto,productoAdmin)

class bioeqAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(xt_bioequivalente)
    list_display = ['id_xt_bioequivalente','referencia','bioequivalente']
    search_fields = ['referencia__descripcion','bioequivalente__descripcion']

admin.site.register(xt_bioequivalente,bioeqAdmin)

admin.site.register(xt_unidad_medida_cant)
#admin.site.register(rel_mc_sust)
#admin.site.register(rel_xt_mb_xt_sust)
#admin.site.register(uk_dmd_conceptos)
#admin.site.register(uk_dmd_relationships)
admin.site.register(xt_formas_agrupadas)
admin.site.register(kairos_sustancia)
admin.site.register(kairos_lab)
admin.site.register(kairos_productos)
admin.site.register(kairos_presentaciones)
admin.site.register(kairos_precio)


__author__ = 'ehebel'
