release: python manage.py syncdb && python manage.py makemigrations && python manage.py migrate
web: gunicorn MagnoliaHouseShows.wsgi --log-file -