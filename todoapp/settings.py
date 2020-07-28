import django_heroku
import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY = '*2v^4ywyj6z%mhv6&xoptuvce^sa6!woocza!d!vo_aku=@9qh'
SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0', '*.herokuapp.com']


INSTALLED_APPS = [
    # 'whitenoise.runserver_nostatic',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tasks.apps.TasksConfig',
]

ROOT_URLCONF = 'todoapp.urls'

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'todoapp.wsgi.application'


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'todoits',
#         'USER': 'todoitsuser',
#         'PASSWORD': 'todoitsuser',
#         'HOST': '192.168.168.242',
#         'PORT': '5432',
#     }
# }

DATABASES = {'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))}

LANGUAGE_CODE = 'ru-RU'


django_heroku.settings(locals())


def get_cache():
    environment_ready = all(
        os.environ.get(f'MEMCACHIER_{key}', False)
        for key in ['SERVERS', 'USERNAME', 'PASSWORD']
    )
    if not environment_ready:
        cache = {'BACKEND': 'django.core.cache.backends.locmem.LocMemCache'}
    else:
        servers = os.environ['MEMCACHIER_SERVERS']
        username = os.environ['MEMCACHIER_USERNAME']
        password = os.environ['MEMCACHIER_PASSWORD']
        cache = {
            'default': {
                'BACKEND': 'django_bmemcached.memcached.BMemcached',
                'TIMEOUT': None,
                'LOCATION': servers,
                'OPTIONS': {
                    'username': username,
                    'password': password,
                }
            }
        }
    return cache
CACHES = get_cache()

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache_table',
    }
}



# https://docs.djangoproject.com/en/3.0/howto/static-files/
# STATIC_DIR = os.path.join(BASE_DIR, "static")
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
