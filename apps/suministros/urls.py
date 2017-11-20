from django.conf.urls import url

from .viewstotal.ordencompra import *
from .viewstotal.requerimiento import *
from .viewstotal.modelocompatible import *
from .viewstotal.suministro import *
from .viewstotal.color import *
from .viewstotal.pedido import *

urlpatterns = [

    # COLORES
    url(r'^color$', ColorVista.as_view(), name="color_inicio"),
    url(r'^color/agregar/$', ColorCrear.as_view(), name="color_crear"),
    url(r'^color/editar/(?P<pk>\d+)$', ColorEditar.as_view(), name="color_editar"),
    url(r'^color/eliminar/(?P<pk>\d+)$', ColorEliminar.as_view(), name="color_eliminar"),

    # SUMINISTROS
    url(r'^suministro$', SuministroVista.as_view(), name="suministro_inicio"),
    url(r'^suministro/agregar/$', SuministroCrear.as_view(), name="suministro_crear"),
    url(r'^suministro/editar/(?P<pk>\d+)$', SuministroEditar.as_view(), name="suministro_editar"),
    url(r'^suministro/eliminar/(?P<pk>\d+)$', SuministroEliminar.as_view(), name="suministro_eliminar"),

    # COMPATIBILIDAD DE MODELOS
    url(r'^modelocompatible$', ModeloCompatibleSuministroVista.as_view(), name="modelocompatible_inicio"),
    url(r'^modelocompatible/tabla/$', ModeloCompatibleTablaVista.as_view(), name="modelocompatible_tabla"),
    url(r'^modelocompatible/listar/(?P<sum>\d+)$', ModeloCompatibleListar.as_view(), name="modelocompatible_listar"),
    url(r'^modelocompatible/agregar/(?P<sum>\d+)$', ModeloCompatibleCrear.as_view(), name="modelocompatible_crear"),
    url(r'^modelocompatible/eliminar/(?P<pk>\d+)$', ModeloCompatibleEliminar.as_view(), name="modelocompatible_eliminar"),
    # url(r'^suministro/eliminar/(?P<pk>\d+)$', SuministroEliminar.as_view(), name="suministro_eliminar"),

    # REQUERIMIENTO
    url(r'^requerimiento$', RequerimientoVista.as_view(), name="requerimiento_inicio"),
    url(r'^requerimiento/tabla/(?P<pk>\d+)$', RequerimientoTablaVista.as_view(), name="requerimiento_tabla"),
    url(r'^requerimiento/listar/(?P<uO>\d+)$', RequerimientoDetalleListar.as_view(), name="requerimiento_listar"),

    # url(r'^requerimiento/filadetalle/(?P<fila>\d+)$', RequerimientoDetalleAgregar.as_view(), name="requerimiento_detalle_agregar"),
    url(r'^requerimiento/agregar/$', RequerimientoUnidadOrganicaVista.as_view(), name="requerimiento_crear"),
    url(r'^requerimiento/agregar/(?P<uO>\d+)$', RequerimientoCrear.as_view(), name="requerimiento_crear"),
    url(r'^requerimiento/eliminar/(?P<pk>\d+)$', RequerimientoEliminar.as_view(),
        name="requerimientoDetalle_eliminar"),


    # ORDEN COMPRA
    url(r'^ordencompra$', OrdenCompraVista.as_view(), name="ordencompra_inicio"),
    url(r'^ordencompra/agregar/$', OrdenCompraCrear.as_view(), name="ordencompra_crear"),
    url(r'^ordencompra/editar/(?P<pk>\d+)$', OrdenCompraEditar.as_view(), name="ordencompra_editar"),
    url(r'^ordencompra/eliminar/(?P<pk>\d+)$', OrdenCompraEliminar.as_view(), name="ordencompra_eliminar"),

    # ORDEN COMPRA DETALLE
    url(r'^ordencompra/detalletabla/$', OrdenCompraDetalleVista.as_view(), name="ordencompradetalle_tabla"),
    url(r'^ordencompra/detalleagregar/$', OrdenCompraDetalleCrear.as_view(), name="ordencompradetalle_crear"),
    url(r'^ordencompra/detallelistar/(?P<ord>\d+)$', OrdenCompraDetalleListar.as_view(), name="ordencompradetalle_listar"),

    #PEDIDOS
    url(r'^pedido$', PedidoVista.as_view(), name="pedido_inicio"),
    url(r'^pedido/agregar/$', PedidoCrear.as_view(), name="pedido_crear"),
    url(r'^pedido/editar/(?P<pk>\d+)$', PedidoEditar.as_view(), name="pedido_editar"),
    url(r'^pedido/eliminar/(?P<pk>\d+)$', PedidoEliminar.as_view(), name="pedido_eliminar"),

]

