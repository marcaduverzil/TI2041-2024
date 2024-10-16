from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Vista para registrar usuarios
def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente
            return redirect('index')  # Redirigir a la página principal
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/register.html', {'form': form})

# Vista para iniciar sesión
def iniciar_sesion(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirigir a la página principal
    else:
        form = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'form': form})

# Vista para cerrar sesión
def cerrar_sesion(request):
    logout(request)
    return redirect('index')  # Redirigir a la página principal
