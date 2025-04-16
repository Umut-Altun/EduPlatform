from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Content, Category, Comment
from .forms import ContentForm, CommentForm

def content_list(request):
    contents = Content.objects.all()
    categories = Category.objects.all()
    
    # Filter by category
    category_id = request.GET.get('category')
    if category_id:
        contents = contents.filter(category_id=category_id)
    
    # Filter by content type
    content_type = request.GET.get('type')
    if content_type:
        contents = contents.filter(content_type=content_type)
    
    # Search
    search_query = request.GET.get('search')
    if search_query:
        contents = contents.filter(title__icontains=search_query) | \
                  contents.filter(description__icontains=search_query)
    
    # Sorting
    sort_by = request.GET.get('sort', 'newest')
    if sort_by == 'newest':
        contents = contents.order_by('-created_at')
    elif sort_by == 'oldest':
        contents = contents.order_by('created_at')
    elif sort_by == 'popular':
        contents = contents.order_by('-likes')
    
    context = {
        'contents': contents,
        'categories': categories,
        'active_category': category_id,
        'active_type': content_type,
        'active_sort': sort_by,
        'search_query': search_query,
    }
    return render(request, 'content_sharing/content_list.html', context)

@login_required
def content_create(request):
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES)
        if form.is_valid():
            content = form.save(commit=False)
            content.author = request.user
            
            # Etiketleri al ve temizle
            tags = request.POST.get('tags', '').strip()
            if tags:
                # Virgülle ayrılmış etiketleri temizle ve kaydet
                tags = ','.join(tag.strip() for tag in tags.split(',') if tag.strip())
                content.tags = tags
                
            content.save()
            return redirect('content_sharing:detail', content.id)
    else:
        form = ContentForm()
    
    return render(request, 'content_sharing/content_form.html', {'form': form})

@login_required
def content_detail(request, pk):
    content = get_object_or_404(Content, pk=pk)
    comments = content.comments.all()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.content = content
            comment.author = request.user
            comment.save()
            content.comments_count = content.comments.count()
            content.save()
            return redirect('content_sharing:detail', pk=pk)
    else:
        comment_form = CommentForm()
    
    context = {
        'content': content,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'content_sharing/content_detail.html', context)

@login_required
def like_content(request, pk):
    content = get_object_or_404(Content, pk=pk)
    
    if request.user in content.likes.all():
        content.likes.remove(request.user)
        liked = False
    else:
        content.likes.add(request.user)
        liked = True
    
    return JsonResponse({
        'liked': liked,
        'likes_count': content.likes.count(),
    })

@login_required
def content_edit(request, pk):
    content = get_object_or_404(Content, pk=pk)
    
    if content.author != request.user:
        raise PermissionDenied("Bu içeriği düzenleme yetkiniz yok.")
    
    if request.method == 'POST':
        form = ContentForm(request.POST, request.FILES, instance=content)
        if form.is_valid():
            content = form.save(commit=False)
            
            # Etiketleri güncelle
            tags = request.POST.get('tags', '').strip()
            if tags:
                tags = ','.join(tag.strip() for tag in tags.split(',') if tag.strip())
                content.tags = tags
            else:
                content.tags = ''
            
            content.save()
            messages.success(request, "İçerik başarıyla güncellendi.")
            return redirect('settings:my_content')
    else:
        form = ContentForm(instance=content)
    
    return render(request, 'content_sharing/content_form.html', {
        'form': form,
        'content': content,
        'edit_mode': True
    })

@login_required
def content_delete(request, pk):
    content = get_object_or_404(Content, pk=pk)
    
    # Check if the user is the author of the content
    if content.author != request.user:
        raise PermissionDenied("Bu içeriği silme yetkiniz yok.")
    
    if request.method == 'POST':
        content.delete()
        messages.success(request, "İçerik başarıyla silindi.")
        return redirect('settings:my_content')
    
    return render(request, 'content_sharing/content_delete.html', {
        'content': content
    })