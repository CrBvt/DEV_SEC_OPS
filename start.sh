# Start Docker
docker-compose up --build -d

# Wait for Docker
sleep 30

# Migrations
docker-compose exec django_node sh -c "python manage.py makemigrations"
docker-compose exec django_node sh -c "python manage.py migrate"

# Tests
docker exec django_node sh -c "pytest"

# Code Quality
docker exec django_node sh -c "pylint"

# Documentation
docker exec django_node sh -c "cd doc && make html"