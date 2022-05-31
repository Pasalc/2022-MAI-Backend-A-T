up:
	docker-compose up --wait

test: up
	docker-compose exec django_server python3 ./django_web/manage.py test

migrate: up
	docker-compose exec django_server python3 ./django_web/manage.py makemigrations
	docker-compose exec django_server python3 ./django_web/manage.py migrate
