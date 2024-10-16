from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_productos, name='index'),
    path('registrar/', views.registrar_producto, name='registrar'),
    path('resultado/', views.resultado_producto, name='resultado'),
]
