from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    receita = {
        1:'lasanha',
        2:'peixe',
        3:'suco de manga'
    }
    dados = {
        'nome':receita
    }
    return render(request, "index.html", dados)

def receita(request):
    return render(request, "receita.html")
