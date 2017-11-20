from django import forms
from django.utils.encoding import force_text
from django_select2.forms import ModelSelect2Widget

from sarsum.widget.inputcheck import ModelCheckWidget
from ...vista.models import inv_modelos
from ..models import Suministro, ModeloCompatible


class widgetSuministro(ModelSelect2Widget):
    queryset = Suministro.objects.order_by("codigo")
    search_fields = ["tipo__icontains", "modelo__icontains"]
    max_results = 10

    def label_from_instance(self, obj):
        return force_text(obj.tipo) + " - " + force_text(obj.modelo)

class ModeloCompatibleSuministroForm(forms.Form):
    opsum = forms.ModelChoiceField(
        label=u"Suministro",
        queryset=Suministro.objects.all(),
        widget=widgetSuministro(
            attrs={"id": "cbSum","class":"form-control"}
        )
    )

class widgetModelo(ModelSelect2Widget):
    search_fields = ["nombre__icontains"]
    max_results = 10

    def label_from_instance(self, obj):
        return force_text(obj.nombre)

class ModeloCompatibleForm(forms.ModelForm):

    modelo = forms.ModelChoiceField(
        label=u"Modelo",
        queryset=inv_modelos.objects.all(),
        widget=widgetModelo()
    )

    principal = ModelCheckWidget(label=u"Principal", initial=False, textYES="SI", textNO="NO")

    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs.pop('kwargs')
        super(ModeloCompatibleForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs['class'] = 'form-control'



        idsum = self.kwargs.get("sum", 0)
        self.fields["modelo"].widget.queryset = inv_modelos.objects.all(
        ).filter(
            marca=Suministro.objects.get(pk=idsum).marca
        ).exclude(
            pk__in=ModeloCompatible.objects.filter(
                suministro_id=idsum
            ).values("modelo_id")
        ).order_by("nombre")





    class Meta:
        model = ModeloCompatible
        fields = ["modelo", "principal"]

    def clean(self):
        self.instance.suministro_id = self.kwargs.get("sum", 0)

