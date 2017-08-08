"""
Django settings for echo_site project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
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

os.environ['PYTHON_EGG_CACHE'] = '/tmp'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gythbpdpfm*yigopappnqhge+z&3y=i)bvhj1nwushg4b=jfu-'

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = True
DEBUG = False
#TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #crispy app
    'crispy_forms',
    'echo',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'echo_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'echo_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'echosite',
	'USER': 'echoadmin',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (

    os.path.join(BASE_DIR, 'static'),
)

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



#App settings
CRISPY_TEMPLATE_PACK = 'bootstrap3'

#login_required URL
LOGIN_URL = '/login/'
