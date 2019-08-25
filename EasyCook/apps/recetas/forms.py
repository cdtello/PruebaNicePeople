from django import forms
from apps.recetas.models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = [
            'categoria',
            'titulo',
            'descripcion',
            'pasos',
            'imagen',
            'precio',
        ]
        labels = {
            'categoria'         : 'Categoria',
            'titulo'            : 'Titulo',
            'descripcion'       : 'Descripcion',
            'pasos'             : 'Pasos',
            'imagen'            : 'Imagen',
            'precio'            : 'Precio',
        }
        widgets = {
            'categoria'         :forms.Select(attrs={'class':'form-control'}),
            'titulo'            :forms.TextInput(attrs={'class':'form-control'}),
            'descripcion'       :forms.TextInput(attrs={'class':'form-control'}),
            'pasos'             :forms.Textarea(attrs={'class':'form-control'}),
            'imagen'            :forms.FileInput(attrs={'class':'form-control'}),
            'precio'            :forms.NumberInput(),
        }