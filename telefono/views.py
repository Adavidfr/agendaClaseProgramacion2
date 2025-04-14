from django.shortcuts import render
from django.http import HttpResponse

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
