from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages  # Corrigido: import oficial do Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm 

from .models import Post
from .forms import PostForm

def post_list(request):
    """Lista todos os posts publicados."""
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, "blog/post_list.html", {"posts": posts})

def post_new(request):
    """Cria um novo post e redireciona para a lista."""
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now() 
            post.save()
            return redirect('post_list') # Redirecionamento corrigido
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def login_view(request):
    """Gere o acesso do usuário ao blog."""
    if request.user.is_authenticated:
        return redirect('post_list') # Redirecionamento corrigido
    
    form = AuthenticationForm()
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                next_url = request.POST.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('post_list') # Redirecionamento corrigido
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
    
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    """Realiza o logout e volta para a tela de login."""
    logout(request)
    return redirect('login') # Garanta que 'login' exista no seu urls.py