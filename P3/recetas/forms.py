from django import forms

from .models import Receta, Ingrediente, Foto

class RecetaForm(forms.ModelForm):

    class Meta:
        model = Receta
        fields = ('__all__')

class IngredienteForm(forms.ModelForm):

    class Meta:
        model = Ingrediente
        fields = ('__all__')

class FotoForm(forms.ModelForm):

    class Meta:
        model = Foto
        fields = ('__all__')