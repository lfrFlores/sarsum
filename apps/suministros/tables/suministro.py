# coding=utf-8
from table.columns import Column
from table.utils import Accessor

from sarsum.clases.tabla import DefaultTable, ActionColumn
from ..models import Suministro

class colRendimiento(Column):
    def render(self, obj):
        valor = Accessor(self.field).resolve(obj)
        return str(valor) + " páginas"

class colTipo(Column):
    def render(self, obj):
        return obj.Tipo()

class SuministroTable(DefaultTable):
    tipo = colTipo(field='tipo', header="Tipo", searchable=False)
    codigo = Column(field='codigo', header="Código")
    modelo = Column(field='modelo', header="Modelo")
    rendimiento = colRendimiento(field='rendimiento', header="Rendimiento")
    marca = Column(field='marca.nombre', header="Marca")
    color = Column(field='color.nombre', header="Color")
    action = ActionColumn("suministros:suministro_editar", "suministros:suministro_eliminar")

    class Meta(DefaultTable.Meta):
        model = Suministro
        id = "suministroTabla"
        attrs = dict(DefaultTable.Meta.attrs.items() + {
            'dataUrlAdd': '/suministros/suministro/agregar/'
        }.items())

