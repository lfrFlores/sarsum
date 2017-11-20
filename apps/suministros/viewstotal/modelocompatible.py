# coding=utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView, CreateView, DeleteView
from table.views import FeedDataView

from ..models import ModeloCompatible
from ..tables.modelocompatible import ModeloCompatibleTabla
from ..formstotal.modelocompatible import ModeloCompatibleSuministroForm, ModeloCompatibleForm


class ModeloCompatibleSuministroVista(FormView):
    template_name = "suministros/modelocompatible/suministro.html"
    form_class = ModeloCompatibleSuministroForm

    def get_context_data(self, **kwargs):
        data = super(ModeloCompatibleSuministroVista, self).get_context_data(**kwargs)
        data["formSum"] = data.get("form")
        return data

class ModeloCompatibleTablaVista(TemplateView):
    template_name = "suministros/modelocompatible/tabla.html"

    def render_to_response(self, context, **response_kwargs):
        context["tablaModeloCompatible"] = ModeloCompatibleTabla(context)
        _result = super(ModeloCompatibleTablaVista, self).render_to_response(context, **response_kwargs)
        return _result

class ModeloCompatibleListar(FeedDataView):
    token = ModeloCompatibleTabla.token

    def get_queryset(self):
            return super(ModeloCompatibleListar, self).get_queryset().filter(suministro_id=self.kwargs.get("sum", 0))

class ModeloCompatibleCrear(CreateView):
    model = ModeloCompatible
    form_class = ModeloCompatibleForm
    template_name = "suministros/modelocompatible/formulario.html"
    titulo_ventana = "Agregando Modelo Compatible"

    def get_form_kwargs(self):
        kwargs = super(ModeloCompatibleCrear, self).get_form_kwargs()
        kwargs["kwargs"] = self.kwargs
        return kwargs

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(ModeloCompatibleCrear, self).render_to_response(context, **response_kwargs)
        return result

    def form_valid(self, form):
        super(ModeloCompatibleCrear, self).form_valid(form)
        msg = {}
        msg['msg'] = "Creado Correctamente"
        msg['value'] = True
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def form_invalid(self, form):
        super(ModeloCompatibleCrear, self).form_invalid(form)
        return render(self.request, self.template_name, {'form': form, 'titulo_ventana': self.titulo_ventana})

class ModeloCompatibleEliminar(DeleteView):
    model = ModeloCompatible
    form_class = ModeloCompatibleForm
    template_name = "suministros/modelocompatible/eliminar.html"
    titulo_ventana = "¿Desea eliminar este Modelo Compatible?"

    def get_success_url(self):
        pass

    def delete(self, request, *args, **kwargs):
        msg = {}
        msg['msg'] = "Eliminado Correctamente"
        msg['value'] = True
        try:
            self.get_object().delete()
        except Exception as e:
            msg['value'] = False
            return render(request, self.template_name,
                          {'object': self.get_object(), 'delete_error': str(e), 'titulo_ventana': self.titulo_ventana})
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(ModeloCompatibleEliminar, self).render_to_response(context, **response_kwargs)
        return result


