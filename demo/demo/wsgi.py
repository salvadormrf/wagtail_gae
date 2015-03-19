"""
WSGI config for demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

LIBS_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# Add lib folder
sys.path.insert(2, os.path.join(LIBS_DIR, 'lib'))


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demo.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
