from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola!!!")


def saludo_con_input(request):
    nombre = input("Dime tu nombre: ")
    return HttpResponse(f"Hola {nombre}")


def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"<h1>{apellido}</h1><h2>{nombre}</h2>")


def fecha_hora(request):
    from datetime import datetime

    ahora = datetime.now().strftime(r"%d/%m/%Y  %H:%M:%S.%f")
    return HttpResponse(f"Fecha y hora: {ahora}")


def numero_aleatorio(request):
    import random

    numero = random.randint(1, 6)
    if numero == 6:
        return HttpResponse(f"<h1>Has tirado el dado: 🎲{numero} ✨ Suerte! </h1>")
    else:
        return HttpResponse(f"<h1>Has tirado el dado: 🎲{numero}</h1> <br> Sigue intentando...")
