web: gunicorn cuiquer.wsgi --log-file - --timeout 120
worker: python manage.py celery worker -B -l info