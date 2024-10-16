from django import forms
from .models import Producto

# Formulario para gestionar productos
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'marca', 'categoria', 'caracteristicas']
