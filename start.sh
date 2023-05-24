echo "Start Docker"
docker-compose up --build -d

echo "Wait for Docker"
sleep 30

echo "Migrations"
docker-compose exec django_node sh -c "python manage.py makemigrations"
docker-compose exec django_node sh -c "python manage.py migrate"

echo "Tests"
docker exec django_node sh -c "pytest"

echo "Code Quality"
docker exec django_node sh -c "pylint"

echo "Documentation"
docker exec django_node sh -c "cd doc && make html"