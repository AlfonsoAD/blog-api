"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

from django.core.wsgi import get_wsgi_application
import os
import sys
sys.path.append('/home/django_projects/blog')
sys.path.append('/home/django_projects/blog/blog')


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')

application = get_wsgi_application()
