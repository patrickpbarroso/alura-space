from django.shortcuts import render, redirect
from apps.usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth, messages

def login(request):
    # View para realizar login de usuário existente na aplicação
    if request.user.is_authenticated:
        return redirect('index')
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome = form["nome_login"].value()
            senha = form["senha"].value()
        
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome} logado com sucesso')
            return redirect('index')
        else:
            messages.error(request, 'Não foi possível realizar login, tente novamente')
            return redirect('login')

    return render(request, 'usuarios/login.html', {"form": form, "where":"login"})

def cadastro(request):
    # View para realizar cadastro de novo usuário na aplicação
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            nome_de_usuario = form["nome_cadastro"].value()
            primeiro_nome = form["primeiro_nome"].value()
            sobrenome = form["sobrenome"].value()
            email = form["email"].value()
            senha = form["senha_1"].value()

            if User.objects.filter(username=nome_de_usuario).exists():
                messages.error(request, 'Usuário já existe.')
                return redirect('cadastro')

            usuario = User.objects.create_user(
                username=nome_de_usuario,
                first_name=primeiro_nome,
                last_name=sobrenome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastro efetuado com sucesso')
            return redirect('login')
    
    return render(request, 'usuarios/cadastro.html', {"form": form})

def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout realizado com sucesso')
    return redirect('login')
