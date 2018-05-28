from .base import *

DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

try:
    from .local import *
except ImportError:
    pass
