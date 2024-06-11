from django.shortcuts import render


def inicio(request):
  context = {
    "nombre": "pepe",
    "apellido": "la rana"
  }
  # conectar a db
  # lógica
  # formatear
  return render(request, "inicio.html", context=context)