[![Tests](https://github.com/williamcanin/crud-django-cbv/actions/workflows/tests.yml/badge.svg)](https://github.com/williamcanin/crud-django-cbv/actions/workflows/tests.yml)

## About

CRUD Django using Class Based-Views. Through NPM, the SASS preprocessor was used to write the stylesheet, Gulp to manage static file tasks like SASS, CSS and Javascript. The project also has setup to deploy on Heroku.

## Requirements

* Python >= 3.9
* Pip >= 21.2
* Poetry >= 1.1.8
* Npm >= 6.14
* PostgreSQL >= 13.4
* libpq-dev (Ubuntu and derivatives)

## Using

```shell
$ poetry shell
$ poetry install
$ npm install
$ npm run assets
$ npm run env
(Edit file .env connection database)
$ npm run server
```

To development:

```shell
$ npm run dev
```

## Create new apps

```shell
$ npm run app <NAME APP>
```


## Heroku

**Deploy:**

```
$ python manage.py collectstatic
$ poetry export -f requirements.txt --output requirements.txt --without-hashes --dev
$ git add .
$ git commit -m "Update"
$ git checkout -b main
$ heroku apps:create <APP NAME>
$ heroku create <APP NAME> --buildpack heroku/nodejs
$ heroku config:set DISABLE_COLLECTSTATIC=1
$ heroku config:set SECRET_KEY="<SECRET_KEY>"
$ heroku config:set DEBUG=False
$ heroku config:set ALLOWED_HOSTS="localhost, 127.0.0.1,  <APP NAME>.herokuapp.com"
$ heroku config:set USE_NPM_INSTALL=true
$ heroku config:set NODE_MODULES_CACHE=true
$ git push -u heroku main
$ heroku ps:scale web=1
$ heroku run python manage.py makemigrations
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku run python manage.py collectstatic
```

**Reset DB:**
```
$ heroku pg:reset DATABASE_URL
$ heroku run python manage.py migrate
```

> NOTE: O Heroku executa seu aplicativo em dynos e os dynos entram em suspensão após 30 minutos, se não houver solicitação. Isso faz com que o Heroku não preserve o upload de arquivos de mídia do usuário entre o reinício do dynos. Por isso o projeto habilita a opção de upload de mídias apenas em modo DEBUG = True. See [Discussion](https://stackoverflow.com/questions/41474150/using-heroku-for-django-media-files) and [Doc Heroku](https://devcenter.heroku.com/articles/s3)

> Nota: Antes de realizar o deploy para github, executar "npm run clean"
