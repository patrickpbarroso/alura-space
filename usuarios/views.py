from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    # View para realizar login de usuário existente na aplicação
    form = LoginForms()
    return render(request, 'usuarios/login.html', {"form": form})

def cadastro(request):
    # View para realizar cadastro de novo usuário na aplicação
    form = CadastroForms()
    return render(request, 'usuarios/cadastro.html', {"form": form})
