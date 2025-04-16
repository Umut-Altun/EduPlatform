from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

class Content(models.Model):
    CONTENT_TYPES = (
        ('note', 'Not'),
        ('project', 'Proje'),
        ('assignment', 'Ödev'),
    )
    
    VISIBILITY_CHOICES = (
        ('public', 'Herkese Açık'),
        ('followers', 'Sadece Takipçiler'),
        ('private', 'Özel'),
    )
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='content/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contents')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)  # blank=False yaptık
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPES, default='note')
    visibility = models.CharField(max_length=20, choices=VISIBILITY_CHOICES, default='public')
    tags = models.CharField(max_length=200, blank=True)  # Virgülle ayrılmış etiketler
    likes = models.ManyToManyField(User, related_name='liked_contents', blank=True)
    comments_count = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.content.title}"
