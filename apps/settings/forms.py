from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})
            
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError('Bu e-posta adresi zaten kullanılıyor.')
        return email

class PasswordChangeForm(forms.Form):
    current_password = forms.CharField(
        label='Mevcut Şifre',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mevcut şifrenizi girin'
        })
    )
    new_password = forms.CharField(
        label='Yeni Şifre',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Yeni şifrenizi girin'
        })
    )
    confirm_password = forms.CharField(
        label='Yeni Şifre (Tekrar)',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Yeni şifrenizi tekrar girin'
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if new_password and confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError('Yeni şifreler eşleşmiyor.')
