from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

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
            print(f"\nALERTA!\nEmail:{email} já cadastrado\n")
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

    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        print(f"if request.method == 'POST':")
        print(f'email: {email}')
        print(f'senha: {senha}')

        if email == '' or senha == '':
            print(f'Os campos email ou senha não podem ficar em branco!!!')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            print(f"User.objects.filter(email=email).exists():\nEmail:{email}")
            nome = User.objects.filter(email=email).values_list('username',flat=True).get()
            print(f"nome = User.objects.filter(email=email).values_list('username')")
            print(f"nome = {nome}")

            print(f"user = auth.authenticate(request, username=nome, password=senha):")
            user = auth.authenticate(request, username=nome, password=senha)
            print(f'user: {user}')

            if user is not None:
                auth.login(request, user)
                print(f"Login Realizado com sucesso!!!")
                return redirect('dashboard')
        
    
    return render(request, 'usuarios/login.html')

def dashboard(request):
    print(f'usuarios>views.py>dashboard(request)')
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')

def logout(request):
    print(f'usuarios>views.py>logout(request)')
    auth.logout(request)
    return redirect('index')

def cria_receita(request):
    print(f'usuarios>views.py>cria_receita(request)')

    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        print(f"\nif request.method == 'POST':")
        print(f"nome_receita: {nome_receita}")
        print(f"ingredientes: {ingredientes}")
        print(f"modo_preparo: {modo_preparo}")
        print(f"tempo_preparo: {tempo_preparo}")
        print(f"rendimento: {rendimento}")
        print(f"categoria: {categoria}")
        print(f"foto_receita: {foto_receita}")
        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')
    