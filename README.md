# testUpTraider
## test work for UpTraider company

### Link to task description: 
https://docs.google.com/document/d/1XTnbcXhejyGB-I2cHRiiSZqI3ElHzqDJeetwHkJbTa8/edit

# Description:
Django application that supports tree menu creation. 
Users can register and create their own hierarchy of tree branches, 
select and remove tree tags, delete and create menus.

### Installation

> git clone git@github.com:xxbek/testUpTraider.git

> cd testUpTraider/

First of all create environment file : (near setting.py)
> vim treeTrader/treeTrader/.evn

Environment file example: 
- SECRET_KEY=you-will-never-guess
- DEBUG=0
- DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]
- DB_NAME=tree_menu
- DB_USER=postgres
- DB_PASSWORD=admin
- DB_HOST=db
- DB_PORT=5432
- SQL_ENGINE=django.db.backends.postgresql_psycopg2

** Use DB_HOST=db in case of docker installation.

** Use DB_HOST=localhost(or another db service) in case of local installation. You must also create tree_menu schema.

## Installation ways

### 1. Installation using docker-compose:

- Build
> sudo docker-compose build

- Run
> sudo docker-compose up -d

- Migrate db
> sudo docker-compose exec web python manage.py migrate --noinput

- View the container log in case of errors:
> sudo docker-compose logs -f

- Create a superuser if necessary:
> sudo docker-compose exec web python manage.py createsuperuser

### 2. Installation using docker-hub

In `docker-compose.yml`  delete `build: ./treeTrader` and put it in its place `image: xxbek/tree_menu`

In `- ./treeTrader/treeTrader/.env` put path to your .evn

> sudo docker-compose up -d

> sudo docker-compose exec web python manage.py migrate --noinput


### 3. Installation using conventional local environment and db service:

- Create virtual environment
> python3 -m venv venv

- Activate it
> source venv/bin/activate

> cd treeTrader

- Install python dependences
> (venv) pip install -r requirements.txt

- Migrate db
> python manage.py migrate

- Run server
> python manage.py runserver

### - Service will be available by 127.0.0.1:8000 
### - Registration is required before using the application!