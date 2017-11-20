# coding=utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from ..formstotal.color import ColorForm
from ..models import Color
from ..tables.color import ColorTable


class ColorVista(TemplateView):
    template_name = "suministros/color/inicio.html"
    tablaColor = ColorTable()

    def render_to_response(self, context, **response_kwargs):
        context["tablaColor"] = self.tablaColor
        _result = super(ColorVista, self).render_to_response(context, **response_kwargs)
        return _result

class ColorCrear(CreateView):
    model = Color
    form_class = ColorForm
    template_name = "suministros/color/formulario.html"
    titulo_ventana = "Agregando Color"

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(ColorCrear, self).render_to_response(context, **response_kwargs)
        return result

    def form_valid(self, form):
        super(ColorCrear, self).form_valid(form)
        msg = {}
        msg['msg'] = "Creado Correctamente"
        msg['value'] = True
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def form_invalid(self, form):
        super(ColorCrear, self).form_invalid(form)
        return render(self.request, self.template_name, {'form': form, 'titulo_ventana': self.titulo_ventana})


class ColorEditar(UpdateView):
    model = Color
    form_class = ColorForm
    template_name = "suministros/color/formulario.html"
    titulo_ventana = "Editando Color"

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(ColorEditar, self).render_to_response(context, **response_kwargs)
        return result

    def form_valid(self, form):
        super(ColorEditar, self).form_valid(form)
        msg = {}
        msg['msg'] = "Creado Correctamente"
        msg['value'] = True
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def form_invalid(self, form):
        super(ColorEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {'form': form, 'titulo_ventana': self.titulo_ventana})

class ColorEliminar(DeleteView):
    model = Color
    form_class = ColorForm
    template_name = "suministros/color/eliminar.html"
    titulo_ventana = "¿Desea eliminar este Color?"

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
            return render(request, self.template_name, {'object': self.get_object(), 'delete_error': str(e), 'titulo_ventana': self.titulo_ventana})
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(ColorEliminar, self).render_to_response(context, **response_kwargs)
        return result

