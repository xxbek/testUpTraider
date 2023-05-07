# testUpTraider
## test work for UpTraider company

### Link to task description: 
https://docs.google.com/document/d/1XTnbcXhejyGB-I2cHRiiSZqI3ElHzqDJeetwHkJbTa8/edit

### Installation
1. Using docker-compose

> sudo docker-compose build

> sudo docker-compose up -d

> sudo docker-compose exec web python manage.py migrate --noinput

> sudo docker-compose exec web python manage.py createsuperuser
 
2. Using conventional local environment and db service

> git clone git@github.com:xxbek/testUpTraider.git

> cd testUpTraider/

> python3 -m venv venv

> source venv/bin/activate

> (venv) pip install -r requirements.txt

> gunicorn treeTrader.wsgi:application --bind 0.0.0.0:8000

> 