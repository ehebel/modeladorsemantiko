__author__ = 'ehebel'
from django import forms
from django.core.exceptions import ValidationError

from modeladorFarmacos2.models import xt_pcce


class pcceForm(forms.ModelForm):

    revisar_pcce = forms.CheckboxInput(
        "Revisado",
    )

    class Meta:
        model = xt_pcce

    def __init__(self, *args, **kwargs):

        if kwargs.get('instance'):
            revisado = kwargs['instance'].revisado
            kwargs.setdefault('initial', {})['revisar_pcce'] = revisado

        return super(pcceForm, self).__init__(*args, **kwargs)