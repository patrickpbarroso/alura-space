from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from django.contrib import messages

def index(request):
    # View que retorna a página inicial da galeria
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar a galeria.')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def imagem(request, foto_id):
    # View para página de imagem da galeria
    fotografia = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia})

def buscar(request):
    # View para pesquisar imagens na galeria
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para realizar pesquisas.')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_a_buscar = request.GET['buscar']
        if nome_a_buscar:
            fotografias = fotografias.filter(nome__icontains=nome_a_buscar)
    return render(request, 'galeria/index.html', {'cards': fotografias})