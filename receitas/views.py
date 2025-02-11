from django.shortcuts import get_object_or_404, get_list_or_404, render
from .models import Receita

def index(request):
    receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    print(f'\ndef index() receitas:\n{receitas}\n')
    dados = {
        'receitas': receitas
    }
    print(f'\nreceitas:\n{receitas}\n')
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    print(f'\ndef receita() {receita}')
    receita_a_exibir = {
        'receita' : receita
    }
    print(f'\nreceita_a_exibir: {receita}\n')
    return render(request, 'receita.html', receita_a_exibir)

def buscar(request):

    lista_receitas = Receita.objects.order_by('-date_receita').filter(publicada=True)
    print(f'\nlista_receitas:\n{lista_receitas}')
    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        print(f'\ndef buscar\nnome_a_buscar:{nome_a_buscar}\n')
        if buscar:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_a_buscar)

    dados = {
        'receitas' : lista_receitas
    }
    print(f'\ndados:{dados}\n')

    return render(request, 'buscar.html',dados)