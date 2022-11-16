from django.urls import path
from django.contrib import admin
from horquillas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home,name="home"),
    path('maquinas/', views.maquinas, name="maquinas"),
    path('registrarMaquina/', views.registrarMaquina, name="registrarMaquina"),
    path('maquinas/edicionMaquina/<codigo>', views.edicionMaquina, name="edicionMaquina"),
    path('editarMaquina/', views.editarMaquina, name="editarMaquina"),
    path('maquinas/eliminarMaquina/<codigo>', views.eliminarMaquina, name="eliminarMaquina"),

    path('',views.inicio_sesion,name="inicio_sesion"),
    path("sesion_iniciada/", views.login_inicio, name="sesion_iniciada"),

    path('clientes/', views.clientes,name="cliente"),
    path('registrarCliente/', views.registrarCliente,name="registrarCliente"),
    path('clientes/edicionCliente/<rut>', views.edicionCliente,name="edicionCliente"),
    path('editarCliente/', views.editarCliente,name="editarCliente"),
    path('clientes/eliminarCliente/<rut>', views.eliminarCliente,name="eliminarCliente"),
   
]