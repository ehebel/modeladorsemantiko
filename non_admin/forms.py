from django import forms

import autocomplete_light

from models import Widget

# in the case of this example, we could just have:
# WidgetForm = autocomplete_light.modelform_factory(Widget)
# but we'll not use this shortcut


class WidgetForm(autocomplete_light.ModelForm):
    model = Widget
