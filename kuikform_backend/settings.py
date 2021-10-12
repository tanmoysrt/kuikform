from pathlib import Path
import os, environ

env = environ.Env(
    SECRET_KEY=(str, "django-insecure-(68ggl!jo9g%e8&t=jav^p0+6=+xvrn+g5)oid)8u)q3e1xwg&"),
    DEBUG=(int, 0),
    ENDPOINT=(str, "127.0.0.1"),
    PROTOCOL=(str, "http://"),
    SMTP_USERID=(str, ""),
    SMTP_PASSWORD=(str, ""),
    TAWKTO_ID_SITE=(str, ""),
    TAWKTO_API_KEY=(str, "")
)
environ.Env.read_env()



SECRET_KEY = env('SECRET_KEY')
DEBUG = True if env('DEBUG') == 1 or env('DEBUG') == '1' else False
MAIN_ENDPOINT = env("ENDPOINT")
MAIN_PROTOCOL = env("PROTOCOL")
SMTP_USERID = env("SMTP_USERID")
SMTP_PASSWORD = env("SMTP_PASSWORD")

BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = ["www.kuikform.com",MAIN_ENDPOINT]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'tawkto',
    'form_process.apps.FormProcessConfig',
    'auth_system.apps.AuthSystemConfig',
    'user_dashboard.apps.UserDashboardConfig'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kuikform_backend.urls'

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

WSGI_APPLICATION = 'kuikform_backend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} if DEBUG else {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASS'),
        'HOST': env('DB_HOST')
    }
}

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR.joinpath('static')

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'auth_system.UserProfile'

CORS_ORIGIN_ALLOW_ALL = True

APPEND_SLASH = True

USER_LOGIN_REDIRECT_URL = "/login/"
DASHBOARD_LINK = "/dashboard/"


TAWKTO_ID_SITE = env("TAWKTO_ID_SITE")
TAWKTO_API_KEY = env("TAWKTO_API_KEY")
TAWKTO_IS_SECURE = True

REPLY_TO_ADDRESS = "kuikform@gmail.com"