worker: python manage.py celery worker -B -l info
web: gunicorn cuiquer.wsgi --log-file - --timeout 120