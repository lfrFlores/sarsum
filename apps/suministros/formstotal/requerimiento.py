from crispy_forms.helper import FormHelper
from datetimewidget.widgets import DateWidget
from django import forms
from django.urls import reverse
from django.forms import inlineformset_factory
from django.utils import timezone
from django.utils.encoding import force_text
from django_select2.forms import ModelSelect2Widget, Select2Widget
from ..viewstotal.requerimiento import *

from django.utils.safestring import SafeString


from ...vista.models import siga_dependencias, siga_unidadesorganicas
from ..models import Suministro, Requerimiento, RequerimientoDetalle



class RequerimientoFormMixin(object):

    def __init__(self, *args, **kwargs):
        super(RequerimientoFormMixin, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False

class widgetDependencia(ModelSelect2Widget):
    queryset = siga_dependencias.objects.order_by('nombre')
    search_fields = ["nombre__icontains"]
    max_results = 10

    def label_from_instance(self, obj):
        return force_text(obj.nombre)

class widgetUnidadOrganica(ModelSelect2Widget):
    queryset = siga_unidadesorganicas.objects.filter(noesunidad=False).order_by("nombre")
    search_fields = ["nombre__icontains"]
    max_results = 10

    def label_from_instance(self, obj):
        return force_text(obj.nombre)

class RequerimientoUnidadOrganicaForm(forms.ModelForm):
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

    dependencia = forms.ModelChoiceField(
        label=u"Dependencia",
        queryset=siga_dependencias.objects.all(),
        widget=widgetDependencia()
    )

    unidadorganica = forms.ModelChoiceField(
        label=u"Unidad Organica",
        queryset=siga_unidadesorganicas.objects.all(),
        widget=widgetUnidadOrganica(
            dependent_fields = {'dependencia': 'dependenciasid'},
            attrs={"id":"cbuO","class":"form-control"},
        )
    )

    def __init__(self, *args, **kwargs):
        super(RequerimientoUnidadOrganicaForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            field.widget.attrs['class'] = 'form-control'
        if self.instance.pk == None:
            self.fields["dependencia"].initial = siga_dependencias.objects.get(pk=1)
            self.fields["fecha"].initial = timezone.now().date()

    class Meta:
        model = Requerimiento
        fields = ["fecha", "dependencia", "unidadorganica"]

    # def clean(self):
    #     self.instance.unidadorganica_id = self.kwargs.get("uO", 0)
    #



class widgetSuministro(ModelSelect2Widget):
    queryset = Suministro.objects.order_by("codigo")
    search_fields = ["codigo__icontains", "modelo__icontains"]
    max_results = 10
class widgetRequerimiento(ModelSelect2Widget):
    queryset = Requerimiento.objects.order_by("numero")
    search_fields = ["numero__icontains"]
    max_results = 10

    def label_from_instance(self, obj):
        return force_text(obj.numero)



class widgetRequerimientoDetalle(ModelSelect2Widget):
        search_fields = ["cantidad__icontains"]
        max_results = 10

        def label_from_instance(self, obj):
            return force_text(obj.cantidad)

class RequerimientoDetalleForm(RequerimientoFormMixin, forms.ModelForm):
    suministro = forms.ModelChoiceField(
        label=u"Suministro",
        queryset=Suministro.objects.all(),
        widget=widgetSuministro()
    )
    requerimiento = forms.ModelChoiceField(
        label=u"Requerimiento",
        queryset=Requerimiento.objects.all(),
        widget=widgetRequerimiento()
    )

    #
    # def __init__(self, args, **kwargs):
    #     self.kwargs = kwargs.pop('kwargs')
    #     super(RequerimientoDetalleForm, self).__init__(args, **kwargs)
    #     iduO = args["view"].request.GET.get("opuO", 0)
    #     if self.opts.attrs.__contains__("dataUrlAdd"):
    #         self.opts.attrs = str(self.opts.attrs).split("dataUrlAdd")[0].strip()
    #     self.opts.attrs = SafeString(
    #         self.opts.attrs + ' dataUrlAdd="/suministros/requerimiento/agregar/' + str(iduO) + '"')
    #     self.opts.ajax_source = reverse(viewname="suministros:requerimiento_listar", kwargs={'uO': iduO})

    def __init__(self, *args, **kwargs):
        self.kwargs = kwargs.pop('kwargs')
        super(RequerimientoDetalleForm, self).__init__(*args, **kwargs)
        for i, (fname, field) in enumerate(self.fields.iteritems()):
            # if field.widget.__class__ == forms.NumberInput:
            #     dp = 2 if type(field) == forms.DecimalField else 0
            #     dpe = 0.01 if type(field) == forms.DecimalField else 1
            #     field.widget.attrs = {"class": 'touch-spin', "data-max": "Infinity", "data-decimals": dp,
            #                           "data-step": dpe,
            #                           "style": "text-align:right", "data-forcestepdivisibility": "none"}
            #     if self.instance.pk == None:
            #         field.initial = 0
            # else:
            #     field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['class'] += " col-xs-4"
            field.widget.attrs['class']='form-control'

    #         # ---------------------------------------
            iduO = self.kwargs.get("uO", 0)
            print("idUnidad Organica---->"+ iduO)
            self.fields["suministro"].widget.queryset = Suministro.objects.all(
            ).filter(
            #     unidadorganica=Requerimiento.objects.get(pk=iduO).unidadorganica
            # ).exclude(
            #     pk__in=RequerimientoDetalle.objects.filter(
            #         requerimiento__unidadorganica_id=iduO
            #     ).values("suministro_id")
            )
            # ).order_by("numero")

    #         # --------------------------
    #
    #
    #     fila = args[0].get("fila", 0)
    #     self.fields["cantidad"].widget.attrs["id"] = "det_cantidad_%s" % (fila)
    #     self.fields["suministro"].widget.attrs["id"] = "det_suministro_%s" % (fila)

    class Meta:
        model = RequerimientoDetalle
        fields = ["cantidad", "suministro","requerimiento"]

        # def clean(self):
        #     self.instance.requerimiento__unidadorganica_id = self.kwargs.get("uO", 0)
        #

# RequerimientoDetalleFormSet = inlineformset_factory(Requerimiento, RequerimientoDetalle, form=RequerimientoDetalleForm, extra=0)


