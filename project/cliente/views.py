from django.shortcuts import render


# Create your views here.
def home(request):
    lista_de_notas = [2, 3, 5, 7, 10, 10]
    contexto = {"notas": lista_de_notas}
    return render(request, "cliente/index.html", contexto)
