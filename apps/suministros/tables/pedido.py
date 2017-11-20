# coding=utf-8
from table.columns import Column
from table.utils import Accessor

from sarsum.clases.tabla import DefaultTable, ActionColumn
from ..models import Pedido

from table.columns import Column, DatetimeColumn

class colColor(Column):
    def render(self, obj):
        text = Accessor(self.field).resolve(obj)
        return "<div style='background-color:" + text + "'>&nbsp;</div>"

class PedidoTable(DefaultTable):
    numero = Column(field='numero', header="Número")
    fecha =  DatetimeColumn(field='fecha', header="Fecha", format="%d/%m/%Y")
    action = ActionColumn("suministros:pedido_editar", "suministros:pedido_eliminar")

    class Meta(DefaultTable.Meta):
        model = Pedido
        id = "pedidoTabla"
        attrs = dict(DefaultTable.Meta.attrs.items() + {
            'dataUrlAdd': '/suministros/pedido/agregar/'
        }.items())

