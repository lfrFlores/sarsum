# coding=utf-8
from django import forms

from ..models import Color
import re

class ColorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ColorForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs['class'] = 'form-control'
        self.fields["codigo"].widget.attrs['class'] += ' select-color'

    class Meta:
        model = Color
        fields = ["nombre", "codigo"]

    def clean_codigo(self):
        valor = self.cleaned_data["codigo"]
        if not re.match('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', valor):
            self.add_error("codigo", u"Ingrese un color válido")
        return valor

