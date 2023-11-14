from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

def login(request):
    # View para realizar login de usuário existente na aplicação
    form = LoginForms()
    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    # View para realizar cadastro de novo usuário na aplicação
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            if form["senha_1"].value() != form["senha_2"].value():
                return redirect('cadastro')
        
        nome = form["nome_cadastro"].value()
        email = form["email"].value()
        senha = form["senha_1"].value()

        if User.objects.filter(username=nome).exists():
            return redirect('cadastro')

        usuario = User.objects.create_user(
            username=nome,
            email=email,
            password=senha
        )
        usuario.save()
        return redirect('login')
    
    return render(request, 'usuarios/cadastro.html', {"form": form})

