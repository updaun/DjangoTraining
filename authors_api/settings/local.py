from .base import * #noqa
from .base import env

# SECURITY WARNING: keep the secret key used in production secret!
# python -c "import secrets; print(secrets.token_urlsafe(38))"
SECRET_KEY = env(
    "DJANGO_SECRET_KEY", default="nYJMmDHee1ppq9qkEZlhhZJq6quWDx0O_1WVd3npKzYOZk7ReFs",
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8080",
]