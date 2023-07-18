web: gunicorn alpha_logistics.wsgi
worker: sh setup.sh && celery -A myapp worker --loglevel=info
release: python manage.py migrate
