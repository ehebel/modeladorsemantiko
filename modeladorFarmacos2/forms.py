__author__ = 'ehebel'
from django import forms

import autocomplete_light


from modeladorFarmacos2.models import xt_pcce


class pcceForm(autocomplete_light.ModelForm):
    class Meta:
        model = xt_pcce
