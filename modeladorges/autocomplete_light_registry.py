import autocomplete_light


from modeladorges.models import ciediez,casdiagnostico,casprocedimiento,concepto, oms2008ciediez
from efectorescas.models import conceptosCASporarea,efector
from modeladorFarmacos.models import *
from privilegiosCAS.models import amca, area, intervencion,especialidad,documento,atributo
from snomedct.models import sct_concept


autocomplete_light.register(ciediez, search_fields=('descriptor','^codigo'),
    autocomplete_js_attributes={'minimum_characters': 3,
                                'placeholder': 'diagnostico ...'})

autocomplete_light.register(casdiagnostico, search_fields=('^descripcion',),
    autocomplete_js_attributes={'minimum_characters': 3,
                                'placeholder': 'diagnostico CAS ...'})

autocomplete_light.register(casprocedimiento, search_fields=('^integlosa',),
    autocomplete_js_attributes={'minimum_characters': 3,
                                'placeholder': 'procedimiento CAS ...'},
    widget_js_attributes = {
        # That will set data-max-values which will set widget.maxValues
        'max_values': 6,
        'bootstrap': 'normal',
        }
)
autocomplete_light.register(concepto, search_fields=('fsn',),
    autocomplete_js_attributes={'minimum_characters': 3,
                                'placeholder': 'SNOMED Conceptos .. '})


autocomplete_light.register(oms2008ciediez, search_fields=('descriptor',),
    autocomplete_js_attributes={'minimum_characters': 3,
                                'placeholder': 'CIE-10 ... '})


autocomplete_light.register(conceptosCASporarea, search_fields=('id',),
    autocomplete_js_attributes={'placeholder': 'ID conceptos por area .. '})

autocomplete_light.register(efector, search_fields=('ExamName',),
    autocomplete_js_attributes={'placeholder': 'Efectores.. '})

#autocomplete_light.registration(xt_mb, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'ej. IBUPROFENO + PARACETAMOL '})
#
#autocomplete_light.registration(xt_unidad_dosis_unitaria, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'ej. ampolla, comprimido..'})
#
#autocomplete_light.registration(xt_unidad_medida_unitaria, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'ej. comprimido'})
#
#autocomplete_light.registration(xt_formas_farm, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'ej. comprimido efervescente '})
#
#autocomplete_light.registration(xt_condicion_venta, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'Cond Venta .. '})
#
#autocomplete_light.registration(xt_sustancias, search_fields=('descripcion',),
#    choices=xt_sustancias.objects.filter(estado=False),
#    autocomplete_js_attributes={'placeholder': 'ej. paracetamol'})
#
#autocomplete_light.registration(vmp_hiba, search_fields=('term_vmp',),
#    autocomplete_js_attributes={'placeholder': 'ej. ACARBOSA 50 MG COMPRIMIDO'})
#
#autocomplete_light.registration(vtm_hiba, search_fields =('term_vtm',),
#    autocomplete_js_attributes={'placeholder': 'ej. PREPARADO CON PARACETAMOL'})
#
#autocomplete_light.registration(xt_mc, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'ej. PARACETAMOL 500 MG COMPRIMIDO'})
#
#autocomplete_light.registration(xt_mcce, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'Inserte'})
#
#
#autocomplete_light.registration(rel_xt_mb_xt_sust, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'Rel Medicamentos Clinicos .. '})
#
#autocomplete_light.registration(rel_mc_sust, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'Rel Medicamentos Clinicos .. '})
#
#
#autocomplete_light.registration(xt_pc, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'ej. TAREG 160 MG COMPRIMIDOS RECUBIERTOS (NOVARTIS)'})
#
#
#autocomplete_light.registration(kairos_sustancia, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'ej. Ibuprofeno...'})
#
#
#autocomplete_light.registration(kairos_presentaciones, search_fields=('claveproducto__descripcion',),
#    autocomplete_js_attributes={'placeholder': 'ej. Ginotex'})
#
#autocomplete_light.registration(xt_fp, search_fields=('descripcion',),
#    autocomplete_js_attributes={'placeholder': 'ej. Panadol...'})
#
#
#autocomplete_light.registration(dbnet, search_fields=('producto',),
#    autocomplete_js_attributes={'placeholder': 'Producto DBNET'})
#
#autocomplete_light.registration(atc, search_fields=('atc_desc','cod_atc'),
#    autocomplete_js_attributes={'placeholder': 'Codigo o Desc ATC'})
#
#autocomplete_light.registration(kairos_productos, search_fields=('descripcion',),)

## Aplicacion de Privilegios CAS

autocomplete_light.register(area, search_fields=('area',),
    autocomplete_js_attributes={'placeholder': 'Area'})

autocomplete_light.register(amca, search_fields=('amca_desc','amca_cod',),
    autocomplete_js_attributes={'placeholder': 'AMCA'})

autocomplete_light.register(intervencion, search_fields=('id_intev','interv_glosa',),
    autocomplete_js_attributes={'placeholder': 'Intervencion'})

autocomplete_light.register(documento, search_fields=('documento',),
    autocomplete_js_attributes={'placeholder': 'Documento'})

autocomplete_light.register(atributo, search_fields=('atributo',),
    autocomplete_js_attributes={'placeholder': 'Atributo'})

autocomplete_light.register(especialidad, search_fields=('espe_descripcion',),
    autocomplete_js_attributes={'placeholder': 'Especialidad'})

## Aplicacion para SNOMED-CT

autocomplete_light.register(sct_concept, search_fields=('fullyspecifiedname',), name='concepto',
    autocomplete_js_attributes={'placeholder': 'FNS...'})

#autocomplete_light.registration(sct_concept, search_fields=('fullyspecifiedname',), name='atributo',
#    choices=sct_concept.objects.filter(conceptid='116680003'),
#    autocomplete_js_attributes={'placeholder': 'Atributo...'})

