import autocomplete_light


from modeladorges.models import ciediez,casdiagnostico,casprocedimiento,concepto, oms2008ciediez
from efectoresCAS.models import conceptosCASporarea,efector
from modeladorFarmacos.models import *

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

autocomplete_light.register(xt_mb, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'ej. IBUPROFENO + PARACETAMOL '})

autocomplete_light.register(xt_unidad_dosis_unitaria, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'ej. ampolla, comprimido..'})

autocomplete_light.register(xt_unidad_medida_unitaria, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'ej. comprimido'})

autocomplete_light.register(xt_formas_farm, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'ej. comprimido efervescente '})

autocomplete_light.register(xt_condicion_venta, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'Cond Venta .. '})

autocomplete_light.register(uk_dmd_conceptos, search_fields=('fullyspecifiedname',),
    autocomplete_js_attributes={'placeholder': 'UK DMD .. '})

autocomplete_light.register(xt_sustancias, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'ej. paracetamol'})

autocomplete_light.register(vmp_hiba, search_fields=('term_vmp',),
    autocomplete_js_attributes={'placeholder': 'ej. ACARBOSA 50 MG COMPRIMIDO'})

autocomplete_light.register(vtm_hiba, search_fields =('term_vtm',),
    autocomplete_js_attributes={'placeholder': 'ej. PREPARADO CON PARACETAMOL'})

autocomplete_light.register(xt_mc, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'ej. PARACETAMOL 500 MG COMPRIMIDO'})


autocomplete_light.register(rel_xt_mb_xt_sust, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'Rel Medicamentos Clinicos .. '})

autocomplete_light.register(rel_mc_sust, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'Rel Medicamentos Clinicos .. '})


autocomplete_light.register(xt_pc, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'ej. TAREG 160 MG COMPRIMIDOS RECUBIERTOS (NOVARTIS)'})


autocomplete_light.register(kairos_sustancia, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'ej. Ibuprofeno...'})

autocomplete_light.register(xt_fp, search_fields=('descripcion',),
    autocomplete_js_attributes={'placeholder': 'ej. Panadol...'})