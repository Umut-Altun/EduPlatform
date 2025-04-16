from pathlib import Path

# Proje içindeki yolları şu şekilde oluşturun: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# GÜVENLİK UYARISI: üretimde kullanılan gizli anahtarı gizli tutun!
SECRET_KEY = 'django-insecure-st+)_1+6=n65ev4i(920fuokbuhc#@j#dnxg1g^o5-)xmcz4(8'

# GÜVENLİK UYARISI: üretimde hata ayıklama açıkken çalıştırmayın!
DEBUG = True

# GÜVENLİK UYARISI: üretimde kullanırken gerçek alan adınızı ekleyin
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "yourdomain.com"]

# Uygulama tanımılarınızı burada tanımlayın
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.content_sharing',
    'apps.settings',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'edu_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'edu_platform.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Uluslararasılaştırma ayarları
LANGUAGE_CODE = 'tr'  # en-tr yerine sadece tr kullanın
TIME_ZONE = 'Europe/Istanbul'  # Türkiye saat dilimi
USE_I18N = True  # Uluslararasılaştırma aktif
USE_L10N = True  # Yerelleştirme aktif
USE_TZ = True  # Saat dilimi desteği aktif

# Desteklenen diller
LANGUAGES = [
    ('tr', 'Türkçe'),
    ('en', 'English'),
]

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Media files (User uploaded files)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Kimlik Doğrulama Ayarları
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# Oturum Ayarları
SESSION_COOKIE_AGE = 3600  # 60 minutes
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
