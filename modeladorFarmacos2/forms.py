__author__ = 'ehebel'
from django import forms

import autocomplete_light


from modeladorFarmacos2.models import xt_pcce


class pcceForm(forms.ModelForm):
    descripcion = forms.CharField(widget=forms.TextInput(attrs={'size': 100, 'title': 'Descripcion:',}))
    desc_abreviada = forms.CharField(widget=forms.TextInput(attrs={'size': 100, 'title': 'Descripcion Abreviada:',}))


    class Meta:
        widgets = autocomplete_light.get_widgets_dict(xt_pcce)
        model = xt_pcce
        exclude = ('id_xt_mcce','id_presentacion_kairos','codigo_dbnet')


