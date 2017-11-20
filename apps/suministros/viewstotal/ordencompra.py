# coding=utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView
from table.views import FeedDataView

from ..formstotal.ordencompra import OrdenCompraForm, OrdenCompraDetalleForm
from ..models import OrdenCompra, OrdenCompraDetalle
from ..tables.ordencompra import OrdenCompraTable, OrdenCompraDetalleTable


class OrdenCompraVista(TemplateView):
    template_name = "suministros/ordencompra/inicio.html"
    tablaOrdenCompra = OrdenCompraTable()

    def render_to_response(self, context, **response_kwargs):
        context["tablaOrdenCompra"] = self.tablaOrdenCompra
        _result = super(OrdenCompraVista, self).render_to_response(context, **response_kwargs)
        return _result

class OrdenCompraCrear(CreateView):
    model = OrdenCompra
    form_class = OrdenCompraForm
    template_name = "suministros/ordencompra/formulario.html"
    titulo_ventana = "Agregando Orden de Compra"

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(OrdenCompraCrear, self).render_to_response(context, **response_kwargs)
        return result

    def form_valid(self, form):
        super(OrdenCompraCrear, self).form_valid(form)
        msg = {}
        msg['msg'] = "Creado Correctamente"
        msg['value'] = True
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def form_invalid(self, form):
        super(OrdenCompraCrear, self).form_invalid(form)
        return render(self.request, self.template_name, {'form': form, 'titulo_ventana': self.titulo_ventana})

class OrdenCompraEditar(UpdateView):
    model = OrdenCompra
    form_class = OrdenCompraForm
    template_name = "suministros/ordencompra/formulario.html"
    titulo_ventana = "Editando Orden de Compra"

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(OrdenCompraEditar, self).render_to_response(context, **response_kwargs)
        return result

    def form_valid(self, form):
        super(OrdenCompraEditar, self).form_valid(form)
        msg = {}
        msg['msg'] = "Creado Correctamente"
        msg['value'] = True
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def form_invalid(self, form):
        super(OrdenCompraEditar, self).form_invalid(form)
        return render(self.request, self.template_name, {'form': form, 'titulo_ventana': self.titulo_ventana})

class OrdenCompraEliminar(DeleteView):
    model = OrdenCompra
    form_class = OrdenCompraForm
    template_name = "suministros/ordencompra/eliminar.html"
    titulo_ventana = "¿Desea eliminar esta Orden de Compra?"

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
        result = super(OrdenCompraEliminar, self).render_to_response(context, **response_kwargs)
        return result

class OrdenCompraDetalleVista(TemplateView):
    template_name = "suministros/ordencompra/tabladetalle.html"

    def render_to_response(self, context, **response_kwargs):
        context["tablaOrdenCompraDetalle"] = OrdenCompraDetalleTable(context)
        _result = super(OrdenCompraDetalleVista, self).render_to_response(context, **response_kwargs)
        return _result

class OrdenCompraDetalleListar(FeedDataView):
    token = OrdenCompraDetalleTable.token

    def get_queryset(self):
        return super(OrdenCompraDetalleListar, self).get_queryset().filter(ordencompra_id=self.kwargs.get("ord", 0))

class OrdenCompraDetalleCrear(CreateView):
    model = OrdenCompraDetalle
    form_class = OrdenCompraDetalleForm
    template_name = "suministros/ordencompra/formulariodetalle.html"
    titulo_ventana = "Agregando Orden de Compra Detalle"

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(OrdenCompraDetalleCrear, self).render_to_response(context, **response_kwargs)
        return result

    def form_valid(self, form):
        super(OrdenCompraDetalleCrear, self).form_valid(form)
        msg = {}
        msg['msg'] = "Creado Correctamente"
        msg['value'] = True
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def form_invalid(self, form):
        super(OrdenCompraDetalleCrear, self).form_invalid(form)
        return render(self.request, self.template_name, {'form': form, 'titulo_ventana': self.titulo_ventana})