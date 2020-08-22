from .base import *
import dj_database_url
import django_heroku

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG")

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

ALLOWED_HOSTS = [".ngrok.io", ".herokuapps.com"]

INSTALLED_APPS += ["whitenoise.runserver_nostatic", ]

MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware', ]

DATABASES['default'] = dj_database_url.config(
    conn_max_age=600, ssl_require=True)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Django Storage Dropbox (User Videos and Images)
# https://django-storages.readthedocs.io/en/latest/backends/dropbox.html

DROPBOX_OAUTH2_TOKEN = os.getenv('DROPBOX_OAUTH2_TOKEN')
DEFAULT_FILE_STORAGE = 'storages.backends.dropbox.DropBoxStorage'
django_heroku.settings(locals())

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# # password Email send
# # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.getenv('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PASSWORD')
# PASSWORD_RESET_TIMEOUT_DAYS = 1

# OTP_TWILIO_ACCOUNT = os.getenv('OTP_TWILIO_ACCOUNT')
# OTP_TWILIO_AUTH = os.getenv('OTP_TWILIO_AUTH')
# OTP_TWILIO_CHALLENGE_MESSAGE = 'OTP send to your number...'
# OTP_TWILIO_TOKEN_TEMPLATE = '''
# \nFrom E_library:please don't share your
# otp: {token}
# '''
# OTP_TWILIO_FROM = os.getenv('OTP_TWILIO_FROM')
# OTP_TWILIO_TOKEN_VALIDITY = 360  # otp valid for 5Min


# BOOK_GENRE = [
#     (1, 'Action and adventure'),
#     (2, 'Art'),
#     (3, 'Alternate history'),
#     (4, 'Autobiography'),
#     (5, 'Anthology'),
#     (6, 'Biography'),
#     (7, 'Chick lit'),
#     (8, 'Book review'),
#     (9, 'Children\'s'),
#     (10, 'Cookbook'),
#     (11, 'Comic book'),
#     (12, 'Diary'),
#     (13, 'Coming-of-age'),
#     (14, 'Dictionary'),
#     (15, 'Crime'),
#     (16, 'Encyclopedia'),
#     (17, 'Drama'),
#     (18, 'Guide'),
#     (19, 'Fairytale'),
#     (20, 'Health'),
#     (21, 'Fantasy'),
#     (22, 'History'),
#     (23, 'Graphic novel'),
#     (24, 'Journal'),
#     (25, 'Historical fiction'),
#     (26, 'Math'),
#     (27, 'Horror'),
#     (28, 'Memoir'),
#     (29, 'Mystery Prayer'),
#     (30, 'Paranormal romance'),
#     (31, 'Religion, spirituality and new age'),
#     (32, 'Picture book'),
#     (33, 'Textbook'),
#     (34, 'Poetry'),
#     (35, 'Review'),
#     (36, 'Political thriller'),
#     (37, 'Science'),
#     (38, 'Romance'),
#     (39, 'Self help'),
#     (40, 'Satire'),
#     (41, 'Travel'),
#     (42, 'Science fiction'),
#     (43, 'True crime'),
#     (44, 'Short story'),
#     (45, 'Suspense'),
#     (46, 'Thriller'),
#     (47, 'Young adult')
# ]

# BOOK_EDITION = [
#     (1, '1st'),
#     (2, '2nd'),
#     (3, '3rd'),
#     (4, '4th'),
#     (5, '5th'),
#     (6, '6th'),
#     (7, '7th'),
#     (8, '8th'),
#     (9, '9th'),
#     (10, '10th')
# ]

# LIST_STATE = [
#     ('AP', 'Andhra Pradesh'),
#     ('AR', 'Arunachal Pradesh'),
#     ('AS', 'Assam'),
#     ('BR', 'Bihar'),
#     ('CT', 'Chhattisgarh'),
#     ('GA', 'Goa'),
#     ('GJ', 'Gujarat'),
#     ('HR', 'Haryana'),
#     ('HP', 'Himachal Pradesh'),
#     ('JH', 'Jharkhand'),
#     ('KA', 'Karnataka'),
#     ('KL', 'Kerala'),
#     ('MP', 'Madhya Pradesh'),
#     ('MH', 'Maharashtra'),
#     ('MN', 'Manipur'),
#     ('ML', 'Meghalaya'),
#     ('MZ', 'Mizoram'),
#     ('NL', 'Nagaland'),
#     ('OR', 'Odisha'),
#     ('PB', 'Punjab'),
#     ('RJ', 'Rajasthan'),
#     ('SK', 'Sikkim'),
#     ('TN', 'Tamil Nadu'),
#     ('TG', 'Telangana'),
#     ('TR', 'Tripura'),
#     ('UT', 'Uttarakhand'),
#     ('UP', 'Uttar Pradesh'),
#     ('WB', 'West Bengal'),
#     ('AN', 'Andaman and Nicobar Islands'),
#     ('CH', 'Chandigarh'),
#     ('DB', 'Dadra and Nagar Haveli'),
#     ('DD', 'Daman and Diu'),
#     ('DL', 'Delhi'),
#     ('JK', 'Jammu and Kashmir'),
#     ('LA', 'Ladakh'),
#     ('LD', 'Lakshadweep'),
#     ('PY', 'Puducherry'),
# ]
