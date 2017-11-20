# coding=utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView

from ..tables.pedido import PedidoTable
from ..formstotal.pedido import PedidoForm
from ..models import Pedido
from ..tables.color import ColorTable


class PedidoVista(TemplateView):
    template_name = "suministros/pedido/inicio.html"
    tablaPedido = PedidoTable()

    def render_to_response(self, context, **response_kwargs):
        context["tablaPedido"] = self.tablaPedido
        _result = super(PedidoVista, self).render_to_response(context, **response_kwargs)
        return _result

class PedidoCrear(CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = "suministros/pedido/formulario.html"
    titulo_ventana = "Agregando Pedido"

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(PedidoCrear, self).render_to_response(context, **response_kwargs)
        return result

    def form_valid(self, form):
        super(PedidoCrear, self).form_valid(form)
        msg = {}
        msg['msg'] = "Creado Correctamente"
        msg['value'] = True
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def form_invalid(self, form):
        super(PedidoCrear, self).form_invalid(form)
        return render(self.request, self.template_name, {'form': form, 'titulo_ventana': self.titulo_ventana})


class PedidoEditar(UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = "suministros/Pedido/formulario.html"
    titulo_ventana = "Editando Pedido"

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(PedidoEditar, self).render_to_response(context, **response_kwargs)
        return result

    def form_valid(self, form):
        super(PedidoEditar, self).form_valid(form)
        msg = {}
        msg['msg'] = "Creado Correctamente"
        msg['value'] = True
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def form_invalid(self, form):
        super(PedidoEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {'form': form, 'titulo_ventana': self.titulo_ventana})

class PedidoEliminar(DeleteView):
    model = Pedido
    form_class = PedidoForm
    template_name = "suministros/pedido/eliminar.html"
    titulo_ventana = "¿Desea eliminar este Pedido?"

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
        result = super(PedidoEliminar, self).render_to_response(context, **response_kwargs)
        return result

