from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contacto

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
    if request.method == 'POST':
        contacto.delete()
        return redirect('lista_contactos'), {'contacto': contacto}
    return render(request, 'eliminar_contacto.html', {'contacto': contacto})    

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
