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

# Deploy Django App to Heroku
 
This is a part of YouTube Tutorial video on How to Deploy a Django Application to Heroku.
https://youtu.be/V2rWvStauak

## Usage

* If you don't have git installed, follow this [Tutorial](https://www.atlassian.com/git/tutorials/install-git) and come back here.

* Make a copy of your project or use a seperate git branch.

* Make sure your virtual environment is activated.

* Add your dependencies to requirements.txt by typing in the terminal,
```shell
pip freeze > requirements.txt
```

* Add this in settings.py
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
```

* [Make a Heroku account](https://signup.heroku.com/)

* [Download Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)

* [Configure Django Heroku](https://devcenter.heroku.com/articles/django-app-configuration)

* In your terminal, type in
 ```shell
git init
git add .
git commit -m "first commit"

heroku login
heroku create app_name
git push heroku main
heroku open

heroku run python manage.py migrate
```
** PS: if Heroku isn't recognized as a command, please close your terminal and editor and then re-open it.

* DEBUG = False in settings.py

* ALLOWED_HOSTS = ['your_app_name.herokuapp.com', 'localhost', '127.0.0.1'] in settings.py

* If you make edits, then just type in the terminal,
```shell
git add .
git commit -m "edit"
git push heroku main
```

# CELERY INSTRUCTIONS 
start the server redis-server
Install globally if needed brew install redis(apple only)
redis-ping
brew service start redis

## celery worker and beat scheduler
 ```shell
celery -A nottodo_project worker -l info
```
*remember to add name of project*
 ```shell
celery -A nottodo_project worker -l info
```

 ```shell
celery -A nottodo_project beat -l info
```
*remember to add name of project* celery -A nottodo_project beat -l info

NB: 

 ```shell
pip install django-celery-results
```
*This should have already have been installed*

 ```shell
python manage.py migrate django_celery_results
```
Monitor Celery Tasks
Run the Celery worker and beat scheduler to monitor tasks:
 ```shell
celery -A nottodo_project worker --loglevel=info
```

 ```shell
celery -A nottodo_project beat --loglevel=info
```

This setup ensures you can track and verify that emails are being sent successfully from your local development environment.




## Installing Redis on Ubuntu
### Step 1: Update System Packages
Before installing Redis, it’s a good idea to update your package lists:
 ```shell
sudo apt update
```
### Step 2: Install Redis
Install Redis by running the following command:
 ```shell
sudo apt install redis-server
```
### Step 3: Verify Redis Installation
Once installed, you can check that Redis is running with:
 ```shell
redis-cli ping
```
If Redis is running, it will return a PONG response.
How to see the time of the celery worker:

ps aux | grep 'celery worker'

gmail. 
ttce yivp isry eljx