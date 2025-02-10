from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def cadastro(request):
    print(f'\nusuarios>views.py>cadastro(request)')

    if request.method == 'POST':
        print(f"if request.method == 'POST'")

        nome = request.POST['nome']
        email = request.POST['email']
        senha = request.POST['password']
        senha2 = request.POST['password2']

        print(f'Verificção de dados preenchidos:')
        print(f'nome: {nome}')
        print(f'email: {email}')
        print(f'senha: {senha}')
        print(f'senha2: {senha2}')

        if not nome.strip():
            print(f"O campo nome não pode ficar em branco...")
            return redirect('cadastro')
        if not email.strip():
            print(f"O campo email não pode ficar em branco...")
            return redirect('cadastro')
        if senha!=senha2:
            print(f"As senhas digitadas não são iguais...")
            return redirect('cadastro')
        if User.objects.filter(email=email).exists():
            print(f"Email:{email} já cadastrado")
            return redirect('cadastro')
        
        print(f"Após verificações, será criado o user em banco de dados...")
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        
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