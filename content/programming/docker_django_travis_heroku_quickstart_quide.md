Title: DOCKER: Docker/Django/Travis/Heroku quickstart quide.
Date: 2016-07-04 19:45
Modified: 
Category: Programming
Tags: Django,  Docker,  Travis,  Heroku
Slug: docker_django_travis_heroku_quickstart_quide
Lang: ru
Authors: znotdead
Summary: Docker/Django/Travis/Heroku quickstart quide.

### Docker/Django/Travis/Heroku quickstart quide.
### Install Docker
Install 'Docker' as in docs (https://docs.docker.com/linux/step_one/):
```
curl -fsSL https://get.docker.com/ | sh
```

To run without sudo:
```
sudo usermod -aG docker `whoami`
```

Get docker Django image:
```
docker pull django
```

### Useful docker commands

View all containers:
```
docker ps --all
```

Run docker

Get to bash console:
```
docker run --rm -it django /bin/bash
```

Get postgres console:
```
docker run -it --rm --link some-postgres:postgres postgres psql -h postgres -U postgres
```

Remove containers and images:
```
docker ps -f 'status=exited' -q | xargs docker rm
docker images -f dangling=true -q | xargs docker rmi
```
### Start Django project

Create django project:
```
docker run django django-admin.py startproject <projectname>
```

### Docker compose

Install docker compose
```
sudo pip install docker-compose
```

Create project dir
In this dir create `Dockerfile`, `requirements.txt` and `docker-compose.yml`
`Dockerfile`
```
FROM django:latest

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
```

`requirements.txt`
```
Django
psycopg2
```

`docker-compose.yml`
```
version: "2"
services:
  db:
    image: "postgres"
    volumes:
      - "pg_data:/var/lib/postgresql/data"

  web:
    build: "."
    user: "1000:1000"
    volumes:
      - ".:/code"
    ports:
      - "8000:8000"
    links:
      - "db"

volumes:
  pg_data:
```

Create new Django project:
```
docker-compose run --rm web django-admin.py startproject <projectname> .
sudo chown -R $USER:$USER .
```

`settings.local.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

### Docker compose useful commands

To rebuild image:
```
docker-compose build
```
or
```
docker-compose up --build
```

Run docker compose:
```
docker-compose up
```

Create app:
```
docker-compose run --rm web python manage.py startapp <app_name>
```

Run tests:
```
docker-compose run web python manage.py test
```

Run migrations:
```
docker-compose run --rm web python manage.py migrate --settings=<projectname>.settings.local
```

Run webserver:
```
docker-compose run --rm -p 8000:8000 web python manage.py runserver 0.0.0.0:8000
```

### Setup Heroku
```
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh
heroku login
heroku ps:scale web=1 --app <heroku_app_name>
heroku config:set DJANGO_SETTINGS_MODULE=settings.heroku
```

`wsgi.py`
```
import os

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<projectname>.settings.heroku")

application = get_wsgi_application()
application = DjangoWhiteNoise(application)
```

`Procfile`
```
web: gunicorn <projectname>.wsgi --log-file -
```

`runtime.txt`
```
python-3.5.1
```

`settings.heroku.py`
```
import dj_database_url

from .base import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = [('user', 'user@gmail.com')]

DATABASES['default'] = dj_database_url.config()

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

ALLOWED_HOSTS = [".herokuapp.com", ]
```

Run migrations on heroku:
```
heroku run --app <heroku_app_name> python manage.py showmigrations --settings=<projectname>.settings.heroku
heroku run --app <heroku_app_name> python manage.py migrate --settings=<projectname>.settings.heroku
```


### Setup Travis

`settings.travis.py`
```
from .base import *


if 'TRAVIS' in os.environ:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'HOST': 'localhost',
            'PORT': 5432,
        }
    }
```
