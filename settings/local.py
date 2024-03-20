from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
         'OPTIONS': {
            "read_default_file":"settings/my.cnf"},
    }
}