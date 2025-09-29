from pathlib import Path

# Base directory of this mini Django project (folder containing this settings.py)
BASE_DIR = Path(__file__).resolve().parent

SECRET_KEY = 'dev-insecure-secret-key-for-django-models-project'
DEBUG = True
ALLOWED_HOSTS = []

# Use the custom user model
AUTH_USER_MODEL = 'bookshelf.CustomUser'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'relationship_app',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

# We keep ROOT_URLCONF and TEMPLATES minimal; not strictly required for non-web commands.
ROOT_URLCONF = 'urls'
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'
LOGIN_REDIRECT_URL = "list_books"
# Let LogoutView render the provided logout template (no redirect)
LOGOUT_REDIRECT_URL = None

TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Run migrations
import os
os.system('python manage.py makemigrations')
os.system('python manage.py migrate')