# DEV SEC OPS
![SelfLearning](https://img.shields.io/badge/self_learning-black?style=for-the-badge)
![Training](https://img.shields.io/badge/Training-black?style=for-the-badge)

## Project Technologies

![Python](https://img.shields.io/badge/Python-v3.9-brightgreen?style=for-the-badge&logo=Python)
![Django](https://img.shields.io/badge/Django-v4.2-red?style=for-the-badge&logo=Django)
![Docker](https://img.shields.io/badge/Docker-v4.19-blue?style=for-the-badge&logo=docker)  

## Python Libraries

![Python-Lib](https://img.shields.io/badge/Pytest_Django-v4.5-orange?style=for-the-badge&logo=pytest) ![Python-Lib](https://img.shields.io/badge/Factory_Boy-v3.2-orange?style=for-the-badge&logo=)
![Python-Lib](https://img.shields.io/badge/Sphinx-v6.2-blueviolet?style=for-the-badge&logo=readthedocs) ![Python-Lib](https://img.shields.io/badge/Pylint-v2.17-lightgrey?style=for-the-badge&logo=)

## About

Self-learning project on good practices in software development, deployment and securing  
Featuring a trivial Django application operating in a Docker network


## Requirements

- Docker

## Installation

1. Download the latest relase : https://github.com/CrBvt/DEV_SEC_OPS/releases/latest
2. Extract the archive  
3. Use a terminal to move into the extracted directory  
4. Under Linux use : ```bash start.sh```  Under Windows use : ```start.bat```
5. Tests, quality checks and documentation generation are executed on every start
6. Django app is started on : http://localhost:8000/

## Evolution

When the project is modified and features are added, the start script is a multistage operation that will operate :
- Tests
- Code quality check
- Documentation generation


This allows an easy tracking of project health after every modification and keeps the project documentation up-to-date

## Tests ![Python-Lib](https://img.shields.io/badge/Pytest_Django-v4.5-orange?style=flat-square&logo=pytest) ![Python-Lib](https://img.shields.io/badge/Factory_Boy-v3.2-orange?style=flat-square&logo=)

Tests are realised thanks to **pytest-django** and fixture are provided by **factory-boy**

Each app of the django project contains its test folder with every test related to this app

pytest-django provides easy testing through **assert** keyword as well as default **client** fixture for django which 
allows operation on the django app such as reaching endpoint or sending request with very few code lines

## Documentation ![Python-Lib](https://img.shields.io/badge/Sphinx-v6.2-blueviolet?style=flat-square&logo=readthedocs)  

Documentation is generated with **sphinx**  
  
It creates a read-the-doc like html tree which allows anyone to
navigate the project source code and seek information through it  

Documentation of the **django project** can be read within the app through the "Read The Docs" button 

Project documentation root folder is located at **django-node/doc**


## Code Quality ![Python-Lib](https://img.shields.io/badge/Pylint-v2.17-lightgrey?style=flat-square)

Quality of the code is evaluated by **pylint**  
Settings of the linter is within **.pylintrc** at the project root

A note above 9/10 should be expected to maintain a reliable code quality



## Links


- Sphinx : https://www.sphinx-doc.org/en/master/

- Pytest : https://readthedocs.org/projects/pytest/

- Pytest-django : https://www.sphinx-doc.org/en/master/

- Factory-boy : https://factoryboy.readthedocs.io/en/stable/

- Pylint : https://pylint.readthedocs.io/en/latest/

- Django self-served doc : https://django-docs.readthedocs.io/en/latest/