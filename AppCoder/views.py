from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso

# Create your views here.
def curso(self):
    curso = Curso(nombre='Desarrollo Web', comision='18989')
    curso.save()
    documentoDeTexto=f'--> Curso: {curso.nombre} Comision: {curso.comision}'
    return HttpResponse(documentoDeTexto)

