# forms.py
from django import forms
from .models import UsuarioDispositivo

class RegistroDispositivoForm(forms.ModelForm):
    class Meta:
        model = UsuarioDispositivo
        fields = ['dispositivo_id', 'alias']

    def clean(self):
        cleaned_data = super().clean()
        dispositivo_id = cleaned_data.get('dispositivo_id')
        alias = cleaned_data.get('alias')

        if UsuarioDispositivo.objects.filter(dispositivo_id=dispositivo_id).exists():
            self.add_error('dispositivo_id', 'Este dispositivo ya está registrado.')

        return cleaned_data
