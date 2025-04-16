from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

@login_required
def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not username or not password:
            messages.error(request, 'Lütfen tüm alanları doldurun!')
            return render(request, 'auth/login.html')
        
        # Önce e-posta ile kontrol et
        try:
            user_obj = User.objects.get(email=username)
            username = user_obj.username
        except User.DoesNotExist:
            # E-posta bulunamadıysa kullanıcı adıyla devam et
            pass
            
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            messages.success(request, f'Hoş geldiniz, {user.get_full_name() or user.username}!')
            return redirect(next_url)
        else:
            messages.error(request, 'E-posta/Kullanıcı adı veya şifre hatalı!')
            return render(request, 'auth/login.html')
            
    return render(request, 'auth/login.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if not all([username, email, password1, password2, first_name, last_name]):
            messages.error(request, 'Lütfen tüm alanları doldurun!')
            return render(request, 'auth/register.html')
            
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu kullanıcı adı zaten kullanılıyor!')
            return render(request, 'auth/register.html')
            
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Bu e-posta adresi zaten kayıtlı!')
            return render(request, 'auth/register.html')
            
        if password1 != password2:
            messages.error(request, 'Şifreler eşleşmiyor!')
            return render(request, 'auth/register.html')
            
        if len(password1) < 8:
            messages.error(request, 'Şifre en az 8 karakter olmalıdır!')
            return render(request, 'auth/register.html')
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                first_name=first_name,
                last_name=last_name
            )
            messages.success(request, 'Hesabınız başarıyla oluşturuldu! Şimdi giriş yapabilirsiniz.')
            return redirect('login')
            
        except Exception as e:
            messages.error(request, 'Hesap oluşturulurken bir hata oluştu!')
            return render(request, 'auth/register.html')
            
    return render(request, 'auth/register.html')

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Başarıyla çıkış yaptınız!')
    return redirect('login')
