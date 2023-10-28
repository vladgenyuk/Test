from python:3.11

expose 8000

run mkdir /app

workdir /app

copy requirements.txt .

run pip install -r requirements.txt

copy . .

workdir social

<<<<<<< HEAD
cmd gunicorn --bind 0.0.0.0:8000 social.wsgi
=======
cmd gunicorn --bind 0.0.0.0:8000 social.wsgi
>>>>>>> 86242b3fccfba32dd195a6b360c45def6fe08d18
