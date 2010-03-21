import os

PROJECT_ROOT = os.path.dirname(__file__)
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
MEDIA_URL = '/media'
ADMIN_MEDIA_PREFIX = '/admin_media/'
SITE_ID = 1
ROOT_URLCONF = 'tekpress.urls'
TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
USE_I18N = True
SECRET_KEY = '@9u-$6ee3x%uarcbn+c!4fw)nfb*#wnd(his&+m14tna1f7sk*'
COMMENTS_APP='tekrecaptcha'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.media',
    'django.core.context_processors.auth',
    'navbar.context_processors.navbar',
    'navbar.context_processors.navbars',
    'navbar.context_processors.crumbs',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_DIRS = (
  os.path.join(PROJECT_ROOT, "templates"),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.comments',
    'django_extensions',
    'navbar',
    'tagging',
    'google_analytics',
    'robots',
    'contact_form',
    'debug_toolbar',
    'tekblog',
    'tekrecaptcha',
)

try:
   from local_settings import *
except ImportError:
   pass

