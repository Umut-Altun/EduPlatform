from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserProfileForm
from apps.content_sharing.models import Content

@login_required
def settings_home(request):
    return render(request, 'settings/settings_home.html')

@login_required
def profile_settings(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profil bilgileriniz başarıyla güncellendi.')
            return redirect('settings:profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'settings/profile.html', {'form': form})

@login_required
def password_settings(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Şifreniz başarıyla değiştirildi.')
            return redirect('settings:password')
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'settings/password.html', {'form': form})

@login_required
def user_content(request):
    # Get all content created by the current user
    contents = Content.objects.filter(author=request.user)
    
    # Filter by content type if specified
    content_type = request.GET.get('type')
    if content_type:
        contents = contents.filter(content_type=content_type)
    
    context = {
        'contents': contents,
        'active_type': content_type,
    }
    return render(request, 'settings/my_content.html', context)
