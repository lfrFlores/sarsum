# coding=utf-8
from datetimewidget.widgets import DateWidget
from django import forms
from django.utils.encoding import force_text
from django_select2.forms import ModelSelect2Widget

from ..models import OrdenCompra, OrdenCompraDetalle, Suministro,RequerimientoDetalle


class OrdenCompraForm(forms.ModelForm):
    fecha = forms.DateField(
        label=u"Fecha",
        widget=DateWidget(
            usel10n=True,
            bootstrap_version=3,
            options={
                'format': 'dd/mm/yyyy',
                'autoclose': True,
                'clearBtn': 'false',
                'fontAwesome': 'true'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(OrdenCompraForm, self).__init__(*args, **kwargs)
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
        model = OrdenCompra
        fields = ["numero", "siaf", "fecha"]
        labels = {
            "numero":"Número",
            "siaf":"Número SIAF",
            "fecha":"Fecha",
        }

class widgetSuministro(ModelSelect2Widget):
    queryset = Suministro.objects.order_by("codigo")
    search_fields = ["codigo__icontains", "modelo__icontains"]
    max_results = 10

    def label_from_instance(self, obj):
        return force_text(obj.codigo) + " - " + force_text(obj.modelo)
class widgetOrdenCompra(ModelSelect2Widget):
    queryset = OrdenCompra.objects.order_by("numero")
    search_fields = ["numero__icontains"]
    max_results = 10

    def label_from_instance(self, obj):
        return force_text(obj.numero)

class widgetRequerimientoDetalle(ModelSelect2Widget):
    queryset = RequerimientoDetalle.objects.order_by("cantidad")
    search_fields = ["cantidad__icontains"]
    max_results = 10

    def label_from_instance(self, obj):
        return force_text(obj.cantidad)

class OrdenCompraDetalleForm(forms.ModelForm):
    suministro = forms.ModelChoiceField(
        label=u"Suministro",
        queryset=Suministro.objects.all(),
        widget=widgetSuministro(
            attrs={"class": "form-control"}
        )
    )
    ordencompra=forms.ModelChoiceField(
        label=u"OrdenCompra",
        queryset=OrdenCompra.objects.all(),
        widget=widgetOrdenCompra(
            attrs={"class": "form-control"}
        )
    )
    requerimientodetalle = forms.ModelChoiceField(
        label=u"RequerimientoDetalle",
        queryset=RequerimientoDetalle.objects.all(),
        widget=widgetRequerimientoDetalle(
            attrs={"class": "form-control"}
        )
    )

    def __init__(self, *args, **kwargs):
        super(OrdenCompraDetalleForm, self).__init__(*args, **kwargs)
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
        model = OrdenCompraDetalle
        fields = ["suministro","ordencompra","precio","cantidad","requerimientodetalle"]
        labels = {
            "precio":"Precio",
            "cantidad":"Cantidad",

        }
        # labels = {
        #     "cantidad": "Cantidad",
        # }
