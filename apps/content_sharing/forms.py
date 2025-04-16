from django import forms
from .models import Content, Comment, Category

class ContentForm(forms.ModelForm):
    class Meta:
        model = Content
        fields = ['title', 'description', 'file', 'category', 'content_type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Başlık'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Açıklama', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'content_type': forms.Select(attrs={'class': 'form-select'}),
            'file': forms.FileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'title': 'Başlık',
            'description': 'Açıklama',
            'file': 'Dosya',
            'category': 'Kategori',
            'content_type': 'İçerik Türü',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Yorumunuzu yazın...', 'rows': 3}),
        }
        labels = {
            'text': '',
        }
