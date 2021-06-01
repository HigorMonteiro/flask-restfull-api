# Zappts Flask API


A project built with flask-restful following good development practices such as authentication via JWT and creation of unittests.

## Running the app

Preferably, first create a virtualenv and activate it, perhaps with the following command:

Obs: nesse projeto optei por utilizar o poetry um excelente versiones de dependencia, caso não tenha ele instalado veja o link de como instalar:  [poetry.org](https://python-poetry.org/docs/)

```
virtualenv -p python3 venv
source venv/bin/activate
```

Next, run

```
poetry install
```

to get the dependencies.

Next, config your file .env :

```
cp .env-temp.text .env
```

Next, initialize the database

```
flask run update
```

## Running tests

To run the test suite, simply pip install it and run from the root directory like so

```
make test
```

Note: it is necessary to register your email credentials so that the user creation and password redemption flow goes smoothly.

```
MAIL_SENDER="[......]@gmail.com"
MAIL_SERVER="smtp.gmail.com"
MAIL_PORT= 465
MAIL_USERNAME="[......]@gmail.com"
MAIL_PASSWORD="......"
MAIL_USE_TLS=false
MAIL_USE_SSL=true
```

#### Using Docker

Dependencies:

- [docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)

```sh

docker-compose build
docker-compose up -d
docker-compose run web flask db upgrade

```