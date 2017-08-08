"""
WSGI config for echo_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os,sys
sys.path.append('/app/devops/virecho/lib/python27.zip')
sys.path.append('/app/devops/virecho/lib/python2.7')
sys.path.append('/app/devops/virecho/lib/python2.7/plat-linux2')
sys.path.append('/app/devops/virecho/lib/python2.7/lib-tk')
sys.path.append('/app/devops/virecho/lib/python2.7/lib-old')
sys.path.append('/app/devops/virecho/lib/python2.7/lib-dynload')
sys.path.append('/usr/local/lib/python2.7')
sys.path.append('/usr/local/lib/python2.7/plat-linux2')
sys.path.append('/usr/local/lib/python2.7/lib-tk')
sys.path.append('/app/devops/virecho/lib/python2.7/site-packages')
sys.path.append('/app/devops/virecho/lib/python2.7/site-packages/Django-1.9.12-py2.7.egg')
sys.path.append('/app/devops/virecho/lib/python2.7/site-packages/MySQL_python-1.2.3-py2.7-linux-x86_64.egg')
sys.path.append('/app/devops/virecho/lib/python2.7/site-packages/django_crispy_forms-1.6.0-py2.7.egg')
sys.path.append('/app/devops/virecho/lib/python2.7/site-packages/Jinja2-2.7.3-py2.7.egg')
sys.path.append('/app/devops/virecho/lib/python2.7/site-packages/MarkupSafe-0.9.3-py2.7-linux-x86_64.egg')
sys.path.append('/app/devops/virecho/lib/python2.7/site-packages/simplejson-3.6.5-py2.7-linux-x86_64.egg')
sys.path.append('/app/devops/virecho/lib/python2.7/site-packages/ansible-1.9.6-py2.7.egg')
sys.path.append('/app/devops/virecho/lib/python2.7/site-packages/paramiko-1.15.1-py2.7.egg')
sys.path.append('/app/devops/virecho/lib/python2.7/site-packages')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "echo_site.settings")

application = get_wsgi_application()
