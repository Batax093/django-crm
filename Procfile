assets: python manage.py collectstatic --no-input
release: python manage.py migrate
web: gunicorn 'djcrm.wsgi:application'
