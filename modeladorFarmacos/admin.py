import autocomplete_light
autocomplete_light.autodiscover()
from django.forms import TextInput, Textarea
from django.contrib import admin
admin.autodiscover()
from modeladorFarmacos.models import *
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


class SustanciaClinicoInline(admin.TabularInline):
    model = xt_mc.rel_mc.through
    form = autocomplete_light.modelform_factory(rel_mc_sust)
    radio_fields = {
        "estado": admin.HORIZONTAL}

#    formfield_overrides = {
#        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
#        #models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
#    }

class SustanciaBasicoInline(admin.TabularInline):
    model = xt_mb.rel_xt_sust.through
    form = autocomplete_light.modelform_factory(rel_xt_mb_xt_sust)
    radio_fields = {
        "estado": admin.HORIZONTAL}


class bioeqAdminInline(admin.TabularInline):
    model = xt_bioequivalente
    form = autocomplete_light.modelform_factory(xt_pc)
    fk_name = 'referencia'


class xt_sustanciasAdmin (admin.ModelAdmin):
    pass

class mcAdmin (admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(xt_mc)
    inlines = [SustanciaClinicoInline,]
    search_fields = ['descripcion']
    list_display = ['id_xt_mc','descripcion','observacion','med_basico']
    list_filter = ['revisado','consultar','estado']
    list_display_links = ['id_xt_mc','descripcion']
    actions = [export_as_csv]
    readonly_fields=('id_xt_mc',)

    radio_fields = {
                "estado": admin.HORIZONTAL
                ,"consultar": admin.HORIZONTAL
                ,"revisado": admin.HORIZONTAL
                ,"tipo_forma_farm": admin.HORIZONTAL
    }




    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario_creador_id', None) is None:
            obj.usuario_creador_id = request.user
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

class mbAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'100'})}}
    form = autocomplete_light.modelform_factory(xt_mb)
    inlines = [SustanciaBasicoInline,]
    search_fields = ['descripcion']
    list_display = ['xt_id_mb','descripcion','observacion']
    list_filter = ['revisado','consultar','estado']
    list_display_links = ['xt_id_mb','descripcion']
    actions = [export_as_csv]
    readonly_fields=('xt_id_mb',)

    radio_fields = {
        "estado": admin.HORIZONTAL
        ,"consultar": admin.HORIZONTAL
        ,"revisado": admin.HORIZONTAL
    }

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario_creador_id', None) is None:
            obj.usuario_creador_id = request.user
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


class mcceAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(xt_mcce)
    readonly_fields=('id_xt_mcce',)
    radio_fields = {
        "estado": admin.HORIZONTAL
        ,"consultar": admin.HORIZONTAL
        ,"revisado": admin.HORIZONTAL
    }
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario_creador_id', None) is None:
            obj.usuario_creador_id = request.user.id
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
        if formset.model == xt_mcce:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()

class pcAdmin(admin.ModelAdmin):
    inlines = [bioeqAdminInline,]
    form = autocomplete_light.modelform_factory(xt_pc)
    readonly_fields=('id_xt_pc',)
    radio_fields = {
        "estado": admin.HORIZONTAL
        ,"consultar": admin.HORIZONTAL
        ,"revisado": admin.HORIZONTAL
    }
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario_creador_id', None) is None:
            obj.usuario_creador_id = request.user.id
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
        if formset.model == xt_pc:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()


class pcceAdmin(admin.ModelAdmin):
    form = autocomplete_light.modelform_factory(xt_pcce)
    readonly_fields=('id_xt_pcce',)
    radio_fields = {
        "estado": admin.HORIZONTAL
        ,"consultar": admin.HORIZONTAL
        ,"revisado": admin.HORIZONTAL
    }
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'usuario_creador_id', None) is None:
            obj.usuario_creador_id = request.user.id
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
        if formset.model == xt_pcce:
            instances = formset.save(commit=False)
            map(set_user, instances)
            formset.save_m2m()
            return instances
        else:
            return formset.save()



admin.site.register(xt_mc,mcAdmin)
admin.site.register(xt_mcce,mcceAdmin)
admin.site.register(xt_mb,mbAdmin)
admin.site.register(xt_pc,pcAdmin)
admin.site.register(xt_pcce,pcceAdmin)

admin.site.register(xt_bioequivalente)
admin.site.register(xt_sustancias,xt_sustanciasAdmin)

admin.site.register(uk_dmd_conceptos)
admin.site.register(uk_dmd_relationships)
admin.site.register(xt_unidad_dosis_unitaria)
admin.site.register(xt_unidad_medida_unitaria)
admin.site.register(xt_formas_farm)
admin.site.register(xt_condicion_venta)
admin.site.register(kairos_sustancia)
admin.site.register(kairos_lab)
admin.site.register(kairos_productos)
admin.site.register(kairos_presentaciones)
admin.site.register(xt_unidad_potencia)
admin.site.register(rel_mc_sust)
admin.site.register(rel_xt_mb_xt_sust)
admin.site.register(xt_gfp)
admin.site.register(xt_fp)
admin.site.register(xt_laboratorio)
admin.site.register(xt_producto)
admin.site.register(xt_unidad_medida_cant)


__author__ = 'ehebel'
