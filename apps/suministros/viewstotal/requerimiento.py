import json

from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, FormView, DeleteView, DetailView
from easy_formsets_bootstrap.views import FormsetMixin
from table.views import FeedDataView

from apps.vista.models import siga_unidadesorganicas
from  ..formstotal.requerimiento import RequerimientoUnidadOrganicaForm, RequerimientoDetalleForm

from apps.suministros.tables.requerimientoDetalle import RequerimientoDetalleTabla
from ..models import Requerimiento, RequerimientoDetalle
from ..tables.requerimiento import RequerimientoTable


#
# class RequerimientoVistaCrear(FormView):
#     template_name = "suministros/requerimiento/requerimiento.html"
#     form_class = RequerimientoUnidadOrganicaForm
#
#     def get_context_data(self, **kwargs):
#         data = super(RequerimientoVistaCrear, self).get_context_data(**kwargs)
#         data["formReq"] = data.get("form")
#         return data
#
# class RequerimientoTablaVista(TemplateView):
#         template_name = "suministros/requerimiento/tabla.html"
#
#         def render_to_response(self, context, **response_kwargs):
#             context["tablaRequerimiento"] = RequerimientoDetalleTabla(context)
#             _result = super(RequerimientoTablaVista, self).render_to_response(context, **response_kwargs)
#             return _result
# class RequerimientoDetalleListar(FeedDataView):
#         token = RequerimientoDetalleTabla.token
#
#         def get_queryset(self):
#             return super(RequerimientoDetalleListar, self).get_queryset().filter(unidadOrganica_id=self.kwargs.get("uO", 0))
# #
#
#
# INICIO DE REQUERIMIENTO
class RequerimientoVista(TemplateView):
    template_name = "suministros/requerimiento/inicio.html"
    tablaRequerimiento = RequerimientoTable()

    def render_to_response(self, context, **response_kwargs):
        context["tablaRequerimiento"] = self.tablaRequerimiento
        _result = super(RequerimientoVista, self).render_to_response(context, **response_kwargs)
        return _result

    def get_context_data(self, **kwargs):
        data = super(RequerimientoVista, self).get_context_data(**kwargs)
        data["formReq"] = data.get("form")
        return data

class RequerimientoUnidadOrganicaVista(FormView):

    template_name = "suministros/requerimiento/requerimiento.html"
    form_class = RequerimientoUnidadOrganicaForm

    def get_context_data(self, **kwargs):
        data = super(RequerimientoUnidadOrganicaVista, self).get_context_data(**kwargs)
        data["formReq"] = data.get("form")
        return data

class RequerimientoTablaVista(DetailView):
        template_name = "suministros/requerimiento/tabla.html"
        model = siga_unidadesorganicas
        context_object_name = "oUni"

        def render_to_response(self, context, **response_kwargs):
            context["tablaRequerimiento"] = RequerimientoDetalleTabla(self.kwargs)
            _result = super(RequerimientoTablaVista, self).render_to_response(context, **response_kwargs)
            return _result

class RequerimientoDetalleListar(FeedDataView):
    token = RequerimientoDetalleTabla.token


    def get_queryset(self):
        # return super(RequerimientoDetalleListar, self).get_queryset()
        return super(RequerimientoDetalleListar, self).get_queryset().filter(requerimiento__unidadorganica_id=self.kwargs.get("uO", 0))
            #
#


class RequerimientoCrear(CreateView):
    model = RequerimientoDetalle
    form_class = RequerimientoDetalleForm
    template_name = "suministros/requerimiento/formulario.html"
    titulo_ventana = "Agregando requerimiento detalle"

    def get_form_kwargs(self):
        kwargs = super(RequerimientoCrear, self).get_form_kwargs()
        kwargs["kwargs"] = self.kwargs
        return kwargs

    def render_to_response(self, context, **response_kwargs):
        context["titulo_ventana"] = self.titulo_ventana
        result = super(RequerimientoCrear, self).render_to_response(context, **response_kwargs)
        return result

    def form_valid(self, form):
        super(RequerimientoCrear, self).form_valid(form)
        msg = {}
        msg['msg'] = "Creado Correctamente"
        msg['value'] = True
        return HttpResponse(json.dumps(msg), content_type='application/json')

    def form_invalid(self, form):
        super(RequerimientoCrear, self).form_invalid(form)
        return render(self.request, self.template_name, {'form': form, 'titulo_ventana': self.titulo_ventana})

class RequerimientoEliminar(DeleteView):
        model = RequerimientoDetalle
        form_class = RequerimientoDetalleForm
        template_name = "suministros/requerimiento/eliminar.html"

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
                              {'object': self.get_object(), 'delete_error': str(e),
                               'titulo_ventana': self.titulo_ventana})
            return HttpResponse(json.dumps(msg), content_type='application/json')

        def render_to_response(self, context, **response_kwargs):
            # context["titulo_ventana"] = self.titulo_ventana
            result = super(RequerimientoEliminar, self).render_to_response(context, **response_kwargs)
            return result

# class RequerimientoFormMixin(object):
#     model = Requerimiento
#     form_class = RequerimientoForm
#     formsets_class = [RequerimientoDetalleFormSet]
#
# class RequerimientoCrear(RequerimientoFormMixin, CreateView):
#     model= Requerimiento
#     form_class = RequerimientoForm
#     template_name = "suministros/requerimiento/formulario.html"
#     titulo_ventana = "Agregando  Requerimiento"
#
#     def render_to_response(self, context, **response_kwargs):
#         context["titulo_ventana"] = self.titulo_ventana
#         _result = super(RequerimientoCrear, self).render_to_response(context, **response_kwargs)
#         return _result
#
# class RequerimientoEditar(RequerimientoFormMixin, FormsetMixin, UpdateView):
#     is_update_view = True
#     template_name = "suministros/requerimiento/formulario.html"
#
# class RequerimientoDetalleAgregar(TemplateView):
#     template_name = "suministros/requerimiento/detalle.html"
#
#     def get_context_data(self, **kwargs):
#         data = super(RequerimientoDetalleAgregar, self).get_context_data(**kwargs)
#         data["formNumero"] = self.kwargs.get("fila", 0)
#         data["formDetalle"] = RequerimientoDetalleForm(self.kwargs)
#         return data
#
#
# #
