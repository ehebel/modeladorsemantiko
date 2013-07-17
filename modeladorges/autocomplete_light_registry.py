import autocomplete_light


from modeladorges.models import ciediez,casdiagnostico,casprocedimiento


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