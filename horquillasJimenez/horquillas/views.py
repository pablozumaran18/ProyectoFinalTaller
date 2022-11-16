from django.shortcuts import render, redirect
from .models import Maquina,Clientes,inicio
from django.contrib import messages

# Create your views here.

def login_inicio (request):
    rut = request.POST['rut']
    clave = request.POST['clave']

    lista = inicio.objects.all()

    for a in lista:
        if rut == a.rut:
            if clave == a.clave:
                context={'context': 'Sesion iniciada correctamente'}
                return render(request, 'home.html', context)
            context={'context': 'La contraseña es incorrecta'}
            return render(request, 'inicio_sesion.html', context)
        context={'context': 'El rut ingresado no se encuentra registrado'}
        return render(request, 'inicio_sesion.html', context)

def inicio_sesion (request):

    return render(request,'inicio_sesion.html')


def home (request):
    return render(request,"home.html")

def maquinas(request):
    maquinaListados = Maquina.objects.all()
    messages.success(request, 'Maquina listadas!')
    return render(request, "gestionMaquina.html", {"maquina": maquinaListados})


def registrarMaquina(request):
    codigo = request.POST['txtCodigo']
    modelo = request.POST['txtModelo']
    operador = request.POST['txtOperador']
    estado = request.POST['txtEstado']

    Maquina.objects.create(
        codigo=codigo, modelo=modelo, operador=operador,estado=estado)
    messages.success(request, 'Maquina registrada!')
    return redirect('/')


def edicionMaquina(request, codigo):
    maquina = Maquina.objects.get(codigo=codigo)
    return render(request, "edicionMaquina.html", {"maquina": maquina})


def editarMaquina(request):
    codigo = request.POST['txtCodigo']
    modelo = request.POST['txtModelo']
    operador = request.POST['txtOperador']
    estado = request.POST['txtEstado']

    maquina = Maquina.objects.get(codigo=codigo)
    maquina.modelo = modelo
    maquina.operador = operador
    maquina.estado = estado
    maquina.save()

    messages.success(request, 'Maquina actualizada!')

    return redirect('/')


def eliminarMaquina(request, codigo):
    maquina = Maquina.objects.get(codigo=codigo)
    maquina.delete()

    messages.success(request, 'maquina eliminada!')

    return redirect('/')



def clientes (request):
    Clientelist = Clientes.objects.all()
    messages.success(request, 'Clientes listados!')
    return render(request, "gestionClientes.html", {"clientes": Clientelist})

def registrarCliente(request):
    rut = request.POST['txtRut']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    fecha = request.POST['txtFecha']
    monto = request.POST['txtMonto']

    Clientes.objects.create(
        rut=rut, nombre=nombre, apellido = apellido, fecha = fecha, monto = monto)
    messages.success(request, 'Cliente registrada!')
    return redirect('/')

def edicionCliente(request, rut):
    clientes = Clientes.objects.get(rut = rut)
    return render(request, "edicionCliente.html", {"clientes": clientes})

def editarCliente(request):
    rut = request.POST['txtRut']
    nombre = request.POST['txtNombre']
    apellido = request.POST['txtApellido']
    fecha = request.POST['txtFecha']
    monto = request.POST['txtMonto']

    clientes = Clientes.objects.get(rut=rut)
    clientes.rut = rut
    clientes.nombre = nombre
    clientes.apellido = apellido
    clientes.fecha = fecha
    clientes.monto = monto
    clientes.save()

    messages.success(request, 'cliente actualizado!')

    return redirect('/')


def eliminarCliente(request, rut):
    clientes = Clientes.objects.get(rut=rut)
    clientes.delete()

    messages.success(request, 'Cliente eliminado!')

    return redirect('/')

