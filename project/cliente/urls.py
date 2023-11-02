from django.urls import path

from . import views

app_name = "cliente"

urlpatterns = [
    path("", views.home, name="home"),
    path("crear_clientes/", views.crear_clientes, name="crear_clientes"),
    path("busqueda/", views.busqueda, name="busqueda"),
    path("crear_cliente/", views.crear_cliente, name="crear_cliente"),
]
