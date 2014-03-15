from .base import *

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': '',
            'OPTIONS': {
      		'options': '-c search_path=lego'
    		}
	}        
}

ALLOWED_HOSTS = ['.dam.io']

STATIC_ROOT = os.environ.get('STATIC_DIR')
