release: python manage.py make_migrations && python manage.py migrate
web: gunicorn MagnoliaHouseShows.wsgi --log-file -