"""
WSGI config for youarefantastic project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '..')
dotenv_path = os.path.join(dotenv_path, '.env')
load_dotenv(dotenv_path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'youarefantastic.settings')

application = get_wsgi_application()
