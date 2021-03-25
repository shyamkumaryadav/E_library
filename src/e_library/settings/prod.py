from .base import *
import dj_database_url
import django_heroku

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG")
ADMINS = [
    ('Shyamkumar Yadav', os.getenv('EMAIL')),

]
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
}

ALLOWED_HOSTS = ["localhost", ".herokuapps.com"]

INSTALLED_APPS += ["whitenoise.runserver_nostatic", ]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600, ssl_require=True)

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
PASSWORD_RESET_TIMEOUT_DAYS = 1

DROPBOX_OAUTH2_TOKEN = os.getenv('DROPBOX_OAUTH2_TOKEN')
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
django_heroku.settings(locals())
