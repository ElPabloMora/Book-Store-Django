migrate:
	python manage.py migrate --settings=settings.local

runserver: migrate
	python manage.py runserver --settings=settings

makemigrations:
	python manage.py makemigrations --settings=settings.local

createsuperuser:
	python manage.py createsuperuser --settings=settings.local


	