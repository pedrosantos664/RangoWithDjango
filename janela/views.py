from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return render(request, "janela/index.html")

def products(request):
    return render(request, "janela/products.html")

def contact(request):
    return render(request, "janela/contact.html")

def registro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        # Validações
        if not nome or not email or not senha:
            messages.error(request, 'Preencha todos os campos!')
            return redirect('registro')
            
        if senha != confirmar_senha:
            messages.error(request, 'As senhas não coincidem!')
            return redirect('registro')
            
        if User.objects.filter(username=email).exists():
            messages.error(request, 'Este email já está cadastrado!')
            return redirect('registro')
        
        try:
            # Cria o usuário
            user = User.objects.create_user(
                username=email,
                email=email,
                password=senha,
                first_name=nome
            )
            user.save()
            
            # Autentica e loga automaticamente
            user = authenticate(request, username=email, password=senha)
            if user is not None:
                login(request, user)
                messages.success(request, f'Cadastro realizado! Bem-vindo, {nome}!')
                return redirect('index')
            
        except Exception as e:
            messages.error(request, f'Erro ao registrar: {str(e)}')
    
    return render(request, 'janela/registro.html')

def login_view(request):
    # Se usuário já está logado, redireciona
    if request.user.is_authenticated:
        return redirect('index')
        
    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        
        if not email or not senha:
            messages.error(request, 'Preencha todos os campos!')
            return redirect('login')
        
        # Autentica com o sistema do Django
        user = authenticate(request, username=email, password=senha)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.first_name}!')
            return redirect('index')
        else:
            messages.error(request, 'Email ou senha incorretos!')
    
    return render(request, 'janela/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'Você saiu com sucesso!')
    return redirect('index')


@login_required


def check_auth(request):
   
    usuario_autenticado = False
    usuario_nome = None
    usuario_id = None
    
    if 'usuario_id' in request.session:
        usuario_autenticado = True
        usuario_nome = request.session.get('usuario_nome', 'Usuário')
        usuario_id = request.session.get('usuario_id')
    
    return {
        'usuario_autenticado': usuario_autenticado,
        'usuario_nome': usuario_nome,
        'usuario_id': usuario_id,
    }
