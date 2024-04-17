from django import forms
from .models import Publicacion

#Permite la creacion del formulario con los items asignados
class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ('title', 'text',)