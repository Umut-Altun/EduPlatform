"""
edu_platform projesi için WSGI yapılandırması.

WSGI çağrılabilirini ``application`` adlı modül düzeyinde bir değişken olarak gösterir.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'edu_platform.settings')

application = get_wsgi_application()
