$.fn.select2.defaults.set('language', 'es');
$.fn.select2.defaults.set('width', '100%');

if ($.fn.dataTable != undefined) {
    $.extend(true, $.fn.dataTable.defaults, {
        "oLanguage": {
            "sLengthMenu": "_MENU_",
            "sSearch": "",
            "sInfoFiltered": "",
            "sProcessing": "Cargando",
        },
        "autoWidth": true,
        "searchDelay": 800,
    });
}