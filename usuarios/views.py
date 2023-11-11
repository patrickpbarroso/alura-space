from django.shortcuts import render

def login(request):
    # View para realizar login de usuário existente na aplicação
    return render(request, 'usuarios/login.html')

def cadastro(request):
    # View para realizar cadastro de novo usuário na aplicação
    return render(request, 'usuarios/cadastro.html')
