# Django rest framework with docker and postgreSQL


# !!! abandoned lab, postgres not working !!!
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


