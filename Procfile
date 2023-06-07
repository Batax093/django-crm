python manage.py collectstatic --no-input

python manage.py migrate

web: gunicorn 'djcrm.wsgi:application'