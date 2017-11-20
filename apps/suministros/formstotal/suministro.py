from django import forms
from django.utils.encoding import force_text
from django_select2.forms import Select2Widget, ModelSelect2Widget

from ...vista.models import inv_marcas
from ..models import Color, Suministro

class widgetMarca(ModelSelect2Widget):
    queryset = inv_marcas.objects.order_by("nombre")
    search_fields = ["nombre__icontains"]
    max_results = 10

    def label_from_instance(self, obj):
        return force_text(obj.nombre)

class widgetColor(ModelSelect2Widget):
    queryset = Color.objects.order_by("nombre")
    search_fields = ["nombre__icontains"]
    max_results = 10

    def label_from_instance(self, obj):
        return force_text(obj.nombre)

class SuministroForm(forms.ModelForm):
    tipo = forms.ChoiceField(
        label=u"Tipo",
        choices=Suministro.tipoSum,
        widget=Select2Widget(attrs={'data-minimum-results-for-search': 'Infinity'})
    )   
    marca = forms.ModelChoiceField(
        label=u"Marca",
        queryset=inv_marcas.objects.all(),
        widget=widgetMarca
    )
    color = forms.ModelChoiceField(
        label=u"Color",
        queryset=Color.objects.all(),
        widget=widgetColor
    )
    def __init__(self, *args, **kwargs):
        super(SuministroForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            if field.widget.__class__ == forms.NumberInput:
                dp = 2 if type(field) == forms.DecimalField else 0
                dpe = 0.01 if type(field) == forms.DecimalField else 1
                field.widget.attrs = {"class": 'touch-spin', "data-max": "Infinity", "data-decimals": dp,
                                      "data-step": dpe,
                                      "style": "text-align:right", "data-forcestepdivisibility": "none"}
                if self.instance.pk == None:
                    field.initial = 0
            else:
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Suministro
        fields = ["tipo", "codigo","marca","modelo","color","rendimiento"]

