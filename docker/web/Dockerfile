from python:3.6

env PYTHONUNBUFFERED 1

run mkdir /web
workdir /web

add ./web/requirements.txt /web/

run pip install -r requirements.txt

add ./web /web/

env PORT=8000                               \
    ROCKETCHAT_URL="http://localhost:3000"  \
    ALLOWED_HOSTS="localhost"

cmd python manage.py runserver 0.0.0.0:$PORT
