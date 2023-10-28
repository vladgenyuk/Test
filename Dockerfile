from python:3.11

expose 8000

run mkdir /app

workdir /app

copy requirements.txt .

run pip install -r requirements.txt

copy . .

workdir social

cmd gunicorn --bind 0.0.0.0:8000 social.wsgi