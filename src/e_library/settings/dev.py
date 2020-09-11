import os
from .base import *

print("*"*20, "DEVELOPMENT", "*"*20)
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
