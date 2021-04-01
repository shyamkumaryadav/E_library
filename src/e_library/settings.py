import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = os.getenv('SECRET_KEY', 'hldcqlh=m&4qiweblwoaap&-z_-+av@37sp2by-1fizn=6*!(u')

DEBUG = os.getenv('DEBUG') == '1'
ALLOWED_HOSTS = ['*.herokuapps.com', 'localhost', '192.168.0.102', '0.0.0.0', '*',]


ADMINS = [
    ('Shyamkumar Yadav', os.getenv('EMAIL')),

]



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    # Django Extensions
    'django_extensions',
    'import_export',

    # Crispy Form is Best
    'crispy_forms',

    # myApps
    'system',
    'account',
    'django_cleanup',
    "whitenoise.runserver_nostatic",
]



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'e_library.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
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

WSGI_APPLICATION = 'e_library.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if not DEBUG:
    import dj_database_url
    print("*"*20, "online", "*"*20)
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=600, ssl_require=True)


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

TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGE_CODE = 'en'
LANGUAGES = [
    ('en', 'English'),
    ('hi', 'Hindi'),
]

LANGUAGE_COOKIE_NAME = 'library_language'

LOCALE_PATH = (
    os.path.join(BASE_DIR, 'locale'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

# Custome User Model
AUTH_USER_MODEL = 'account.User'

LOGIN_URL = 'account:signin'
LOGIN_REDIRECT_URL = 'system:home'
LOGOUT_REDIRECT_URL = 'account:signin'

# crispy-form
CRISPY_TEMPLATE_PACK = 'bootstrap4'

if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = os.getenv("EMAIL_USER")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_PASSWORD")
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    DEFAULT_FROM_EMAIL = 'Shyamkumar Yadav'

    DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
    DROPBOX_OAUTH2_TOKEN = os.getenv("DROPBOX_TOKEN")
    DROPBOX_ROOT_PATH = '/e_library'
    import django_heroku
    django_heroku.settings(locals())
else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
