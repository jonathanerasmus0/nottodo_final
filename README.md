# Authors

This application was developed as a final project during a one year Python Course in 2024 by 
- [DCI - Digital Career Institute ](https://digitalcareerinstitute.org/).



- Asmaa Shehata https://github.com/AsmaaShehata88,

- Esther Madianga    https://github.com/Estherkarl,

- Jonathan Davies    https://github.com/jonathanerasmus0,

- Pawel Suchocki  https://github.com/suchockipawel

Thank You 
Instructions for creating a .env file once we finalise the POSTGRES database:

1. pip install python-decouple (this must then be added to the requirements.txt as an installed item)
2. create an .env file in the ROOT directory.
DEBUG=True
SECRET_KEY='django-insecure-%j*w)iqgv8)h1gpn8*b28hbe$w6fpz%28wp^8-l4p(&pq&s*s='
DATABASE_URL=postgres://user:password@localhost:5432/dbname

3.  UPDATE settings.py
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'notodo',
        'USER': 'postgres',
        'PASSWORD': 'new_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
