from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from receitas.models import Receita
from django.contrib.auth.models import User
from django.contrib import auth, messages

def busca(request):
    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    print(f'\nlista_receitas:\n{lista_receitas}')
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        print(f'\ndef buscar\nnome_a_buscar:{nome_a_buscar}\n')
        lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas' : lista_receitas
    }
    print(f'\ndados:{dados}\n')

    return render(request, 'receitas/buscar.html',dados)
