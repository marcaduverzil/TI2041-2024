from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    productos = Producto.objects.all()
    return render(request, 'index.html', {'productos': productos})

def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resultado')
    else:
        form = ProductoForm()
    return render(request, 'register.html', {'form': form})

def resultado_producto(request):
    return render(request, 'result.html')
