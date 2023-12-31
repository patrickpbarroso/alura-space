from django.shortcuts import render, get_object_or_404, redirect
from apps.galeria.models import Fotografia
from apps.galeria.forms import FotografiaForms
from django.contrib import messages
import random

def index(request):
    # View que retorna a página inicial da galeria
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar a galeria.')
        return redirect('login')
    
    fotografias = Fotografia.objects.order_by('-data_fotografia').filter(publicada=True)
    return render(request, 'galeria/index.html', {'cards': fotografias, 'where': 'index'})

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

def nova_imagem(request):
    # View para adicionar nova imagem a galeria
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login')
        return redirect('login')
    
    form = FotografiaForms
    if request.method == 'POST':
        form = FotografiaForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Nova fotografia cadastrada!')
            return redirect('index')
    
    return render(request, 'galeria/nova_imagem.html', {'form':form, 'where': 'nova-imagem'})

def editar_imagem(request, foto_id):
    # view para editar imagem
    fotografia = Fotografia.objects.get(id=foto_id)
    form = FotografiaForms(instance=fotografia)

    if request.method == 'POST':
        form = FotografiaForms(request.POST,request.FILES, instance=fotografia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Fotografia editada com sucesso.')
            return redirect('index')

    return render(request, 'galeria/editar_imagem.html', {'form':form,'foto_id':foto_id})

def deletar_imagem(request, foto_id):
    # view para deletar imagem
    fotografia = Fotografia.objects.get(id=foto_id)
    fotografia.delete()
    messages.success(request, 'Fotografia deletada com sucesso.')

    return redirect('index')

def filtro(request, categoria):
    # View para filtrar imagens por categoria
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login')
        return redirect('login')
    fotografias = Fotografia.objects.order_by("data_fotografia").filter(publicada=True, categoria=categoria)
    return render(request, 'galeria/index.html', {'cards': fotografias})

def surpreenda(request):
    # View para retornar uma imagem aleatória da galeria em Surpreenda-me
    ids = Fotografia.objects.values_list('id', flat=True).filter(publicada=True)
    foto_surpresa_id = random.choice(ids)
    fotografia = get_object_or_404(Fotografia, pk=foto_surpresa_id)
    return render(request, 'galeria/imagem.html', {'fotografia': fotografia, 'where':'surpreenda'})