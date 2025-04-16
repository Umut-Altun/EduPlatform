"""
edu_platform projesi için ASGI yapılandırması.
ASGI çağrılabilirini ``application`` adlı modül düzeyinde bir değişken olarak gösterir.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edu_platform.settings')

application = get_asgi_application()
