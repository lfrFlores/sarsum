# coding=utf-8
from table import Table
from table.columns import LinkColumn, Link
from table.utils import A


class DefaultTable(Table):

    class Meta:
        ajax = True
        row_attrs = {'data-id': lambda record: record.pk}
        attrs = {
            'style': 'background-color: #FFF',
            'class': 'table-striped table-bordered table-hover dt-responsive nowrap',
            'width': '100%'
        }
        zero_records = 'Ningun registro'
        pagination = True
        pagination_first = "Primero"
        pagination_prev = "Anterior"
        pagination_next = "Siguiente"
        pagination_last = "Último"
        search_placeholder = "Buscar"
        template_name = 'table_new.html'


def ActionColumn(url_update=None, url_delete=None, url_detalle =None):
    if url_update == None and url_delete == None and url_detalle == None:
        return None
    _result = "LinkColumn(" \
        "searchable=False," \
        "header='Acciones'," \
        "sortable=False," \
        "header_attrs={'width': '60px'}," \
        "attrs={'class': 'text-center', 'style': 'width:100%'}," \
        "links={"
    if url_update != None:
        _result += \
            "Link(" \
            "    attrs={'class': 'fa fa-pencil button', 'title': 'Editar', 'data-toggle': 'modal', " \
            "           'data-target': '#modalMaster'}, " \
            "    text='', " \
            "    viewname=url_update, " \
            "    kwargs={'pk': A('pk')}," \
            "),"
    if url_delete != None:
        _result += \
            "Link(" \
            "    attrs={'class': 'fa fa-trash button', 'title': 'Eliminar', 'data-toggle': 'modal', " \
            "           'data-target': '#modalMaster'}, " \
            "    text='', " \
            "    viewname=url_delete," \
            "    kwargs={'pk': A('pk')}," \
            "),"
    if url_detalle != None:
        _result += \
            "Link(" \
            "    attrs={'class': 'fa fa-chevron-right button', 'title': 'Detalle', " \
            "        'id': 'btnDetalle'   }, "\
            "    text='', "\
            "    viewname=url_detalle," \
            "),"
    _result += "})"
    return eval(_result)

