# Django rest framework with docker and postgreSQL


# !!! postgres not working !!!
> terminal command
- work in repo
**folder/file**

## setup
> $ mkdir drf-api-poermissions-postgres

Use poetry to initialize folder 

> $ cd `drf-api-poermissions-postgres` 
> $ poetry init -n 
> $ poetry add django djangorestframework 
> $ poetry add --dev black 
> $ poetry shell 

> $ django-admin startproject library_api_project .
> $ python manage.py startapp books

**Dockerfile**
**docker-compose.yml**
**requirements.txt**
> $ docker-compose up -d

# SQLite >> PostgreSQL
**db.sqlite3**

> $ code docker-compose
**docker-compose.yml**
```depends_on: 
      - db
  db:
    image: postgres:11
```
> $ docker-compose up -d

> $ docker-compose ps 
  - list containers
> $ docker-compose images 
  - list images

**library_api_project/settings.py**
```DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'db',  # match to service in docker-compose
        'PORT': 5423,
    }
}
```

postgres talks SQL 
pg admin: makes javascript talk sql
psyco pg 2: makes python talk sql
- psycopg2-binary (no compiling) //NO H!!

> $ poetry add psycopg2-binary

> $ poetry export -f requirements.txt -o requirements.txt
                      ^                       ^
                format/file               location

> $ docker-compose up --build -d

migrate is for host machine, we are in container // postgres

**do not migrate until user model is authenticated with admin**

**library/settings.py**
INSTALLED_APPS = ```'books.apps.UsersConfig',```
<!-- ```AUTH_USER_MODEL = 'books.CustomUser'``` -->
```ALLOWED_HOSTS = ['0.0.0.0','localhost','127.0.0.1']```

**books/models.py**
- create custom user class inheriting AbstractUser

**CREATE>> books/forms.py**
- create custom user creation and update forms classes

**books/admin.py**
- create custom user admin 
- register custom user and custom user admin

> $ python manage.py makemigrations
> $ python manage.py migrate


> $ docker-compose exec web python manage.py migrate
      $ docker-compose exec <'name of service/container'>
        - execute a command in a running container

> $ docker-compose exec web python manage.py createsuperuser

-just django stuff on local machine-
**library/settings.py**
- installed apps
- rest frame work

**library/urls.py**

**books/views.py**

create super user
creat non super user

**library/urls**
log in log out
```path('api-auth/', include('rest_framework.urls')),```

**books/permissions.py**
permissions class

**books/views**
set permissions class


# WEB TOKENS
install 
> $ poetry add djangorestframework-simplejwt
*not compatible*

**pyproject.toml**
```python = "~3.8"```
> $ poetry add djangorestframework-simplejwt

**library/settings.py**
defaults
```    'DEFAULT_AUTHENTICATION_CLASSES':[
      'rest_framework_simplejwt.authentication.JWTAuthentication'
    ]
```

**library/urls.py**
``` path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
```

> $ brew install httpie
   - GET is default
> $ http GET localhost:8000
   - no domain assumes localhost


> $ http POST :8000/api/token/ username=griffin password=12345

> $ http :8000/api/v1/ "Authorization: Bearer <'paste token'>"

postman website

superuser cannot see without token 
**library/settings**
```      'rest_framework.authentication.SessionAuthentication',
      'rest_framework.authentication.BasicAuthentication',
```
now the superuser can see without token
  browsable api (see without using django admin)


# PRODUCTION SERVER
**docer-compose.yml**
``` build: .
    # command: python manage.py runserver 0.0.0.0:8000
    command: gunicorn library_api_project.wsgi:application --bind 0.0.0.0:8000 --workers 4
```

local 
then docker with gunicorn

> $ docker-compose up --build -d
now using gunicorn


**library/settings.py** 
> $ poetry add whitenoise  
    development page hides static issues, but production will not hide 
> $ poetry add django-cors-headers 

# KEYS TO ENV
settings

```import os
import environ

env = environ.ENV()
```
**requirements.txt**
install

INSIDE PROJECT FOLDER
**.env**

> $ docker-compose up --build -d
*404 error*

**.env**
set ```DEBUG=off``` in .env

> $ docker-compose restart

> $ docker-compose exec web python manage.py collectstatic
*no file or directory '/code/static/'*

> $ docker-compose exec web bash

> $ python manage.py collectstatic
- static files copied to '/code/staticfiles/'

> $ docker-compose restart

*server 500 error*
DEBUG=on
need to migrate
> $ docker-compose exec web python manage.py migrate

> $ docker-compose exec web python manage.py createsuperuser

these are same command
> $ http GET localhost:8000/api/v1/
> $ http :8000/api/v1/

ssh?
> $ git clone
> $ nano
  edit env from terminal
> $ cat docker-compose 
  4 workers
> $ docker-compose up -d

> $ docker-compose ps 
containers are up bd and web 

> $ cat project/.env
change allowed hosts / ip addresses
*docker error page*
> $ exit 
connection to __ closed
              ^
          IP address needs to be in allowed hosts
> $ nano project/.env
> $ docker-compose restart
*docker error 404*

-heroku
  free
-digital ocean
-linode
-azure