from django.forms.widgets import ClearableFileInput

class MyFileInput(ClearableFileInput):
    initial_text = 'Actual'
    input_text = 'Cambiar'
    clear_checkbox_label = 'Limpiar'