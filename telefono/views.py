from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contacto
from .forms import CustomUserCreationForm, ContactoForm
from django.contrib.auth.views import LoginView


def lista_contactos(request):
    contactos = Contacto.objects.all()
    return render(request, 'lista_contactos.html', {'contactos': contactos})

def agregar_contactos(request):
    if request.method == 'POST':
        nom = request.POST['nombre']
        tel = request.POST['telefono']
        em = request.POST['email']
        Contacto.objects.create(nombre=nom, telefono=tel, email=em)
        return redirect('lista_contactos')
    return render(request, 'agregar_contacto.html')

def editar_contacto(request, id):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save()
            return redirect('lista_contactos')
    else:
        contacto = get_object_or_404(Contacto, id=id)
        form = ContactoForm(instance=contacto)
    return render(request, 'editar_contacto1.html', {'form': form, 'contacto': contacto})

def editar_contacto_old(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    if request.method == 'POST':
        contacto.nombre = request.POST['nombre']
        contacto.telefono = request.POST['telefono']
        contacto.email = request.POST['email']
        contacto.save()
        return redirect('lista_contactos')
    return render(request, 'editar_contactos.html')
    
def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    return redirect('lista_contactos')

def crear_usuario(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_contactos')
        else:
            form = CustomUserCreationForm()
        return render(request, 'registrar.html', {'form': form})
    
class logeo(LoginView):
    template_name = 'loguear.html'
    
  

# Create your views here.
def hola_mundo(request):
    html = """ 
    <html>
    <head>
        <style>
            body {
                background-color: 7ba4b6;
                color: yellow;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 50px;
            }
            input[type="text"] {
                padding: 10px;
                font-size: 16px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <h1>Hola Bienvenido</h1>
        <p>Somos el segundo semestre</p>
        <input type="text" placeholder="Escribe tu nombre aquí" />
        <button>Agregar</button>
    </body>
    </html>
    """
    return HttpResponse(html)
