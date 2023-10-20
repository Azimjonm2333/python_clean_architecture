# Python Clean Architecture

## Quick Start

**NOTE**: The project uses Python 3.11, so need it installed first. It is recommended to use [`pyenv`](https://github.com/pyenv/pyenv) for installation.

**NOTE**: Root of the django project is at the `src` folder

Here is a short instruction on how to quickly set up the project for development:

1. Install [`poetry`](https://python-poetry.org/)
2. Clone
```bash
$ git clone https://github.com/azizjon-aliev/python_clean_architecture.git
```

3. Install requirements:
```bash
$ poetry install
$ poetry shell
```

4. Install pre-commit hooks: `$ pre-commit install`
6. Add and setup .env file: `$ cp .env.example .env` -> edit `.env`
5. Initiate the database: `$ python manage.py migrate`
8. Run the server: `$ python manage.py runserver`

### Run the API backend

Create docker images and execute the containers for development. From the project directory:
```
$ docker-compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml --env-file ./.env up -d --build
```

## Execute tests suite

1. Execute the docker containers with environment variables setup for testing:
```
$ docker-compose -f docker/docker-compose.yml -f docker/docker-compose.test.yml --env-file ./.env up -d --build
```

2. Access running api backend _api_container_ docker container shell:
```
docker exec -it api_container bash
```
3. Execute pytest command from project directory:
```
pytest
```

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job.)

[django]: <https://www.djangoproject.com>
[djangorestframework]: <https://www.django-rest-framework.org>
[postgres]: <https://www.postgresql.org>
[cleanarchitecture]: <https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html>
[swagger]: <https://github.com/sdediego/django-clean-architecture/blob/main/docs/forex.yaml>