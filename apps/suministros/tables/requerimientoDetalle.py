# coding=utf-8
from django.utils.safestring import SafeString
from table.columns import Column, DatetimeColumn
from table.utils import Accessor
from django.urls import reverse

from apps.suministros.tables.modelocompatible import ModeloCompatibleTabla
from ..models import Requerimiento, RequerimientoDetalle
from sarsum.clases.tabla import DefaultTable, ActionColumn

class columRequerimiento(Column):
    def render(self, obj):
        return "%s" % (obj.requerimiento.numero)
class RequerimientoDetalleTabla(DefaultTable):

    requerimiento=columRequerimiento(field='requerimiento',header='Requerimiento')
    suministro=Column(field='suministro',header='Suministro')
    cantidad = Column(field='cantidad', header="Cantidad")
    action = ActionColumn(url_delete="suministros:requerimientoDetalle_eliminar")


    class Meta(DefaultTable.Meta):
        id = "requerimientoTabla"
        model = RequerimientoDetalle

    def __init__(self, args, **kwargs):
        super(RequerimientoDetalleTabla, self).__init__(args, **kwargs)
        iduO = args.get("pk", 0)
        if self.opts.attrs.__contains__("dataUrlAdd"):
            self.opts.attrs = str(self.opts.attrs).split("dataUrlAdd")[0].strip()
        self.opts.attrs = SafeString(self.opts.attrs + ' dataUrlAdd="/suministros/requerimiento/agregar/' + str(iduO) + '"')
        self.opts.ajax_source = reverse(viewname="suministros:requerimiento_listar", kwargs={'uO': iduO})


