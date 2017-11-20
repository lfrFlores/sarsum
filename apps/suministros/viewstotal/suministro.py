# coding=utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from ..formstotal.suministro import SuministroForm
from ..models import Suministro
from ..tables.suministro import SuministroTable


class SuministroVista(TemplateView):
    template_name = "suministros/suministro/inicio.html"
    tablaSuministro = SuministroTable()

    def render_to_response(self, context, **response_kwargs):
        context["tablaSuministro"] = self.tablaSuministro
        _result = super(SuministroVista, self).render_to_response(context, **response_kwargs)
        return _result

class SuministroCrear(CreateView):
    model = Suministro
    form_class = SuministroForm
    template_name = "suministros/suministro/formulario.html"
    titulo_ventana = "Agregando Suministro"

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(SuministroCrear, self).render_to_response(context, **response_kwargs)
        return result

    def form_valid(self, form):
        super(SuministroCrear, self).form_valid(form)
        msg = {}
        msg['msg'] = "Creado Correctamente"
        msg['value'] = True
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def form_invalid(self, form):
        super(SuministroCrear, self).form_invalid(form)
        return render(self.request, self.template_name, {'form': form, 'titulo_ventana': self.titulo_ventana})


class SuministroEditar(UpdateView):
    model = Suministro
    form_class = SuministroForm
    template_name = "suministros/suministro/formulario.html"
    titulo_ventana = "Editando Suministro"

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(SuministroEditar, self).render_to_response(context, **response_kwargs)
        return result

    def form_valid(self, form):
        super(SuministroEditar, self).form_valid(form)
        msg = {}
        msg['msg'] = "Creado Correctamente"
        msg['value'] = True
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def form_invalid(self, form):
        super(SuministroEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {'form': form, 'titulo_ventana': self.titulo_ventana})


class SuministroEliminar(DeleteView):
    model = Suministro
    form_class = SuministroForm
    template_name = "suministros/suministro/eliminar.html"
    titulo_ventana = "¿Desea eliminar este Suministro?"

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
        result = super(SuministroEliminar, self).render_to_response(context, **response_kwargs)
        return result


