import autocomplete_light


from modeladorges.models import ciediez,casdiagnostico,casprocedimiento,concepto, oms2008ciediez
from efectorescas.models import conceptosCASporarea,efector
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

