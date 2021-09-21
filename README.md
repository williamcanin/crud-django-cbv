## Requirements

* Python >= 3.9
* Pip >= 21.2
* Poetry >= 1.1.8
* PostgreSQL >= 13.4

## Using

```shell
$ poetry shell
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


## Deploy Heroku

```
$ heroku apps:create <APP NAME>
$ git add .
$ git commit -m "Update in Heroku"
$ git push heroku master
$ heroku ps:scale web=1
$ heroku run python manage.py makemigrations
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku config:set DEBUG=Fase
```

> NOTE: O Heroku executa seu aplicativo em dynos e os dynos entram em suspensão após 30 minutos, se não houver solicitação. Isso faz com que o Heroku não preserve o upload de arquivos de mídia do usuário entre o reinício do dynos. Por isso o projeto habilita a opção de upload de mídias apenas em modo DEBUG = True. See [Discussion](https://stackoverflow.com/questions/41474150/using-heroku-for-django-media-files) and [Doc Heroku](https://devcenter.heroku.com/articles/s3)

> Nota: Antes de realizar o deploy para github, executar "gulp clean"
