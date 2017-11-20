from django import forms

def ModelCheckWidget(label = "", textYES = "Activo", textNO = "Inactivo", initial=False):
	return forms.BooleanField(
		required=False,
		label=label,
		initial=initial,
		widget=forms.CheckboxInput(
			attrs={
				"data-toggle": "toggle",
				"data-size": "small",
				"data-height": "30",
				"data-onstyle": "primary",
				"data-offstyle": "danger",
				"data-on": "<i class='fa fa-check-square-o'></i> " + textYES,
				"data-off": "<i class='fa fa-ban'></i> " + textNO,
			}
		),
	)
