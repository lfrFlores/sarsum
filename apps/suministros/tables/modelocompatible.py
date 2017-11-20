from django.urls import reverse
from django.utils.safestring import SafeString
from table.columns import Column
from table.utils import Accessor

from ..models import ModeloCompatible
from sarsum.clases.tabla import DefaultTable, ActionColumn


class columnPrincipal(Column):
    def render(self, obj):
        valor = Accessor(self.field).resolve(obj)
        return "Si" if valor == True else "No"

class ModeloCompatibleTabla(DefaultTable):
    modelo = Column(field='modelo.nombre', header="Modelo")
    principal = columnPrincipal(field='principal', header="Principal", header_attrs={'class': 'text-center col-xs-1'})
    action = ActionColumn(url_delete="suministros:modelocompatible_eliminar")

    class Meta(DefaultTable.Meta):
        id = "modeloCompatibleTabla"
        model = ModeloCompatible

    def __init__(self, args, **kwargs):
        super(ModeloCompatibleTabla, self).__init__(args, **kwargs)
        idsum = args["view"].request.GET.get("opsum", 0)
        if self.opts.attrs.__contains__("dataUrlAdd"):
            self.opts.attrs = str(self.opts.attrs).split("dataUrlAdd")[0].strip()
        self.opts.attrs = SafeString(self.opts.attrs + ' dataUrlAdd="/suministros/modelocompatible/agregar/' + str(idsum) + '"')
        self.opts.ajax_source = reverse(viewname="suministros:modelocompatible_listar", kwargs={'sum': idsum})


