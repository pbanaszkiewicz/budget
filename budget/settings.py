import os

import environ

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR is the directory where `manage.py` is located.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Environment variables configuration

env = environ.Env(
    # default types and values
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),
)
# .env is in parent directory to `settings.py`
env_file = os.path.join(BASE_DIR, '.env')
# read from .env file if it exists
environ.Env.read_env(env_file)

DEBUG = env('DEBUG')
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = env('ALLOWED_HOSTS')


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    'django_extensions',
    'django_select2',
    'mathfilters',  # additional math operations in templates
    'expenses.apps.ExpensesConfig',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'budget.urls'

INTERNAL_IPS = [
    '127.0.0.1',
]

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

WSGI_APPLICATION = 'budget.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

PASS_VALID_IMPRT = 'django.contrib.auth.password_validation'
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': f'{PASS_VALID_IMPRT}.UserAttributeSimilarityValidator'},
    {'NAME': f'{PASS_VALID_IMPRT}.MinimumLengthValidator'},
    {'NAME': f'{PASS_VALID_IMPRT}.CommonPasswordValidator'},
    {'NAME': f'{PASS_VALID_IMPRT}.NumericPasswordValidator'},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# added
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# URLs to redirect to after user is logged in / logged out
# (redirects only if `?next_page` is missing)
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
