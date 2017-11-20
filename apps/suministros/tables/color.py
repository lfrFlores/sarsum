# coding=utf-8
from table.columns import Column
from table.utils import Accessor

from sarsum.clases.tabla import DefaultTable, ActionColumn
from ..models import Color

class colColor(Column):
    def render(self, obj):
        text = Accessor(self.field).resolve(obj)
        return "<div style='background-color:" + text + "'>&nbsp;</div>"

class ColorTable(DefaultTable):
    nombre = Column(field='nombre', header="Nombre")
    codigo = Column(field='codigo', header="Código")
    color = colColor(field='codigo', header="Color", searchable=False, sortable=False, header_attrs={'class': 'col-xs-1 text-center'})
    action = ActionColumn("suministros:color_editar", "suministros:color_eliminar")

    class Meta(DefaultTable.Meta):
        model = Color
        id = "colorTabla"
        attrs = dict(DefaultTable.Meta.attrs.items() + {
            'dataUrlAdd': '/suministros/color/agregar/'
        }.items())

