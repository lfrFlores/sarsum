# coding=utf-8
from table.columns import Column, DatetimeColumn

from ..models import Requerimiento, RequerimientoDetalle
from sarsum.clases.tabla import DefaultTable, ActionColumn


class columUnidad(Column):
    def render(self, obj):
        return "%s" % (obj.unidadorganica.nombre)

class RequerimientoTable(DefaultTable):

    numero = Column(field='numero', header="Número")
    fecha = DatetimeColumn(field='fecha', header="Fecha", format="%d/%m/%Y")
    unidadorganica = columUnidad(field='unidadorganica', header="Solicitante")
    cantidad = Column(field='cantidad', header="Cantidad")
    # action = ActionColumn("suministros:requerimiento_editar", "suministros:requerimiento_eliminar")
    class Meta(DefaultTable.Meta):
        model = Requerimiento
        id = "requerimientoTabla"
        attrs = dict(DefaultTable.Meta.attrs.items() + {
            'dataUrlAdd': '/suministros/requerimiento/agregar/'
        }.items())
