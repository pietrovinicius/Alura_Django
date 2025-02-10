from django.shortcuts import render, redirect

def cadastro(request):
    print(f'usuarios>views.py>cadastro(request)')

    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        print(f"if request.method == 'POST':")
        print(f'nome: {nome}')
        print(f'email: {email}')
        print(f'senha: {senha}')
        print(f'senha2: {senha2}')

        print(f'\nUsuario criado com sucesso!\n')
        return redirect('login')
    else:
        print(f'\nUsuario não criado...retornando para cadastro.html\n')
        return render(request, 'usuarios/cadastro.html')

def login(request):
    print(f'usuarios>views.py>login(request)')
    return render(request, 'usuarios/login.html')

def dashboard(request):
    print(f'usuarios>views.py>dashboard(request)')
    pass

def logout(request):
    print(f'usuarios>views.py>logout(request)')
    pass