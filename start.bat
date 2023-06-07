REM Start Docker
docker-compose up --build -d

REM Wait for Docker
REM timeout 30

REM Migrations
docker-compose exec django_node sh -c "python manage.py makemigrations"
docker-compose exec django_node sh -c "python manage.py migrate"

REM Tests
docker exec django_node sh -c "pytest"

REM Code Quality
docker exec django_node sh -c "pylint ../django_node"

REM Documentation
docker exec django_node sh -c "cd docs && make clean && make html"

REM Check me out : http://localhost:8000/
pause