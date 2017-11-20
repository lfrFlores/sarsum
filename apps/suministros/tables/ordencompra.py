# coding=utf-8

from sarsum.clases.tabla import DefaultTable, ActionColumn
from table.columns import Column, DatetimeColumn
from ..models import OrdenCompra, OrdenCompraDetalle
from django.urls import reverse
from django.utils.safestring import SafeString

class OrdenCompraTable(DefaultTable):
    numero = Column(field='numero', header="Número O/C")
    siaf = Column(field='siaf', header="Número SIAF")
    fecha = DatetimeColumn(field='fecha', header="Fecha", format="%d - %m - %Y")
    action = ActionColumn("suministros:ordencompra_editar", "suministros:ordencompra_eliminar", "suministros:ordencompradetalle_tabla")

    class Meta(DefaultTable.Meta):
        model = OrdenCompra
        id = "ordencompraTabla"
        attrs = dict(DefaultTable.Meta.attrs.items() + {
            'dataUrlAdd': '/suministros/ordencompra/agregar/'
        }.items())

class columCantidad(Column):
    def render(self, obj):
        return "%s" % (obj.cantidad)


class OrdenCompraDetalleTable(DefaultTable):
    cantidad = columCantidad(field='cantidad', header="Cantidad")
    suministro = Column(field='sumnistro', header="Suministro")
    precio = Column(field='precio', header="Precio")
    total = Column(field='total', header="Total")
    #action = ActionColumn("suministros:ordencompra_editar", "suministros:ordencompra_eliminar")

    class Meta(DefaultTable.Meta):
        model = OrdenCompraDetalle
        id = "ordencompradetalleTabla"
        attrs = dict(DefaultTable.Meta.attrs.items() + {
            'dataUrlAdd': '/suministros/ordencompra/detalleagregar/'
        }.items())
    """
    def __init__(self, args, **kwargs):
        super(OrdenCompraDetalleTable, self).__init__(args, **kwargs)
        idoc = args["view"].request.GET.get("opsum", 0)
        if self.opts.attrs.__contains__("dataUrlAdd"):
            self.opts.attrs = str(self.opts.attrs).split("dataUrlAdd")[0].strip()
        self.opts.attrs = SafeString(self.opts.attrs + ' dataUrlAdd="/suministros/ordencompra/detalleagregar/' + str(idoc) + '"')
        self.opts.ajax_source = reverse(viewname="suministros:ordencompradetalle_listar", kwargs={'sum': idoc})
    """