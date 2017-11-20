# coding=utf-8
from django import forms

from ..models import Pedido

from django.utils import timezone
from datetimewidget.widgets import DateWidget
import re

class PedidoForm(forms.ModelForm):
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
        super(PedidoForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs['class'] = 'form-control'
            self.fields["fecha"].initial = timezone.now().date()
        # self.fields["numero"].widget.attrs['class'] += ' select-color'

    class Meta:
        model = Pedido
        fields = ["numero", "fecha"]
    #
    # def clean_pedido(self):
    #     valor = self.cleaned_data["numero"]
    #     if not re.match('^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', valor):
    #         self.add_error("codigo", u"Ingrese un color válido")
    #     return valor
    #
