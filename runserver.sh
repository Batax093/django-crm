python manage.py collectstatic --no-input

python manage.py migrate

uvicorn djcrm.asgi:application --host 0.0.0.0 --port $PORT
