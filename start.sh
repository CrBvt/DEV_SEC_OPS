docker-compose up --build

sleep 30

docker-compose exec django_node sh -c "python manage.py makemigrations"
docker-compose exec django_node sh -c "python manage.py migrate"