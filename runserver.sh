python manage.py collectstatic --no-input

python manage.py migrate

gunicorn djcrm.wsgi:application --bind 0.0.0.0:8000
