import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'hldcqlh=m&4qiweblwoaap&-z_-+av@37sp2by-1fizn=6*!(u'
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 'django.contrib.sites',

    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.google',

    # Django Extensions
    'django_extensions',
    # myApps
    'system',
    # App fro Account
    'account',
    # Crispy Form is Best idea
    'crispy_forms',
    'frontend',
]
# SITE_ID = 1

# # Provider specific settings
# SOCIALACCOUNT_PROVIDERS = {
#     'google': {
#         # For each OAuth based provider, either add a ``SocialApp``
#         # (``socialaccount`` app) containing the required client
#         # credentials, or list them here:
#         'APP': {
#             'client_id': '123',
#             'secret': '456',
#             'key': ''
#         }
#     }
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'e_library.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'reactapp/build'),
        ],
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

# AUTHENTICATION_BACKENDS = [
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend',
# ]

WSGI_APPLICATION = 'e_library.wsgi.application'

    # DATABASES = {
    #     'default': {
    #         # pip install psycopg2 in case error $ sudo apt install libpq-dev python3-dev
    #         'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #         'NAME': os.environ['H_DB_NAME'],        'USER': os.environ['H_DB_USER'],
    #         'PASSWORD': os.environ['H_DB_PASSWORD'],
    #         'HOST': os.environ['H_DB_HOST'],
    #     }
    # }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
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
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('hi', 'Hindi'),
    ('ta', 'Tamil'),
    ('te', 'Telugu'),
    ('ur', 'Urdu'),
    ('pa', 'Punjabi'),
    ('mr', 'Marathi'),
    ('bn', 'Bengali'),
]
LANGUAGES_BIDI = ['ur', ]


LOCALE_PATH = (
    os.path.join(BASE_DIR, 'locale'),
)

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'reactapp/build/static'),
)
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Custome User Model
AUTH_USER_MODEL = 'account.User'

LOGIN_URL = 'account:signin'
LOGIN_REDIRECT_URL = 'system:home'
LOGOUT_REDIRECT_URL = 'account:signin'

# crispy-form
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# password Email send
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('EMAIL_USER')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASSWORD')


BOOK_GENRE = [
    (1, 'Action and adventure'),
    (2, 'Art'),
    (3, 'Alternate history'),
    (4, 'Autobiography'),
    (5, 'Anthology'),
    (6, 'Biography'),
    (7, 'Chick lit'),
    (8, 'Book review'),
    (9, 'Children\'s'),
    (10, 'Cookbook'),
    (11, 'Comic book'),
    (12, 'Diary'),
    (13, 'Coming-of-age'),
    (14, 'Dictionary'),
    (15, 'Crime'),
    (16, 'Encyclopedia'),
    (17, 'Drama'),
    (18, 'Guide'),
    (19, 'Fairytale'),
    (20, 'Health'),
    (21, 'Fantasy'),
    (22, 'History'),
    (23, 'Graphic novel'),
    (24, 'Journal'),
    (25, 'Historical fiction'),
    (26, 'Math'),
    (27, 'Horror'),
    (28, 'Memoir'),
    (29, 'Mystery Prayer'),
    (30, 'Paranormal romance'),
    (31, 'Religion, spirituality and new age'),
    (32, 'Picture book'),
    (33, 'Textbook'),
    (34, 'Poetry'),
    (35, 'Review'),
    (36, 'Political thriller'),
    (37, 'Science'),
    (38, 'Romance'),
    (39, 'Self help'),
    (40, 'Satire'),
    (41, 'Travel'),
    (42, 'Science fiction'),
    (43, 'True crime'),
    (44, 'Short story'),
    (45, 'Suspense'),
    (46, 'Thriller'),
    (47, 'Young adult')
]

BOOK_EDITION = [
    (1, '1st'),
    (2, '2nd'),
    (3, '3rd'),
    (4, '4th'),
    (5, '5th'),
    (6, '6th'),
    (7, '7th'),
    (8, '8th'),
    (9, '9th'),
    (10, '10th')
]

LIST_STATE = [
    ('AP', 'Andhra Pradesh'),
    ('AR', 'Arunachal Pradesh'),
    ('AS', 'Assam'),
    ('BR', 'Bihar'),
    ('CT', 'Chhattisgarh'),
    ('GA', 'Goa'),
    ('GJ', 'Gujarat'),
    ('HR', 'Haryana'),
    ('HP', 'Himachal Pradesh'),
    ('JH', 'Jharkhand'),
    ('KA', 'Karnataka'),
    ('KL', 'Kerala'),
    ('MP', 'Madhya Pradesh'),
    ('MH', 'Maharashtra'),
    ('MN', 'Manipur'),
    ('ML', 'Meghalaya'),
    ('MZ', 'Mizoram'),
    ('NL', 'Nagaland'),
    ('OR', 'Odisha'),
    ('PB', 'Punjab'),
    ('RJ', 'Rajasthan'),
    ('SK', 'Sikkim'),
    ('TN', 'Tamil Nadu'),
    ('TG', 'Telangana'),
    ('TR', 'Tripura'),
    ('UT', 'Uttarakhand'),
    ('UP', 'Uttar Pradesh'),
    ('WB', 'West Bengal'),
    ('AN', 'Andaman and Nicobar Islands'),
    ('CH', 'Chandigarh'),
    ('DB', 'Dadra and Nagar Haveli'),
    ('DD', 'Daman and Diu'),
    ('DL', 'Delhi'),
    ('JK', 'Jammu and Kashmir'),
    ('LA', 'Ladakh'),
    ('LD', 'Lakshadweep'),
    ('PY', 'Puducherry'),
]
