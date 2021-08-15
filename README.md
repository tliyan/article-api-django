# Simple Article API

![Markdown](https://img.shields.io/badge/python-v3.8.2-yellow)

A simple Article API written using the Django REST Framework with a Postgres database. 

## Prerequisites
- Docker
- Docker-Compose
- Make

## Setup

The application is completely containerised using `Docker/Docker-Compose` and utilises `make` to manage all lifecycle tasks.

> NOTE: The following tasks assume that you are in the project directory

### Configuring environment files

Templates environment files are provided that lists the various environment variables that are required for each application. This will need to be populated _before_ building and launching the services.

To do this, create a copy of each file in their respective directory, populate the variables accordingly and rename
both files to `.env`. It is critical they are renamed so that docker-compose can pick up the environment file when
spinning up the container. 

> NOTE: The Postgres environment variables need to be the __same__ across both the app environment file and the postgres environment file to ensure that the Django application can connect to the Postgres instance

```
➜  scp ./conf/app/app.env ./conf/app/.env

➜  scp ./conf/db/postgres.env ./conf/db/.env
```

### Building the application 

Building both the Postgres and Django images can be done with one `make` command
```
➜  make build
```

### Starting the application

There are separate `make` commands to spin up each of the services, as given below.
> NOTE: It is pivotal that the Postgres service is spun up and running __before__ starting the Django service to ensure that there is an actively running database for the the Django service to connect to. 
```
# Start Postgres DB in detached mode
➜  make start-db

# Start Django Service
➜  make start-app

```

### Configuring the application

Once both services have been spun up, there are two configuration tasks that need to be run before using the application:

- Migrating the database models
- Creating an admin user

These configuration tasks can be both be run (while the server is running) in a new terminal window using the following `make` command
```
➜  make configure-app
```

## Usage

Once the app has been started and configured using the steps above, it will be available to access at a base url of `localhost:8000` either via `curl` or a REST client.

### Services

The current services that are available are:

- Create an Article
- Get an Article via Article Id
- Get a Tag via Tag Name and Date


### Sample Usage

The following provides sample requests for each of the services outlined in the above section.

Create an Article

```
> POST /articles HTTP/1.1
> Host: localhost:8000
> Content-Type: application/json
> Accept: */*

{
    "title": "Article #1",
	"date": "2016-12-09",
	"body": "Text for an Article",
	"tags": [
		"sport",
		"finance"
	]
}


< HTTP/1.1 201 Created
< Content-Type: application/json

```


Get an Article via Article Id
```
> GET /articles/1 HTTP/1.1
> Host: localhost:8000
> Content-Type: application/json
> Accept: */*


< HTTP/1.1 200 OK
< Content-Type: application/json

{
    "id": "1",
    "title": "Article #1",
    "date": "2016-12-09",
    "body": "Text for an Article",
    "tags": [
        "finance",
        "sport"
    ]
}

```

Get a Tag via Tag Name and Date
```
> GET /tags/sport/20161209 HTTP/1.1
> Host: localhost:8000
> Content-Type: application/json
> Accept: */*


< HTTP/1.1 200 OK
< Content-Type: application/json

{
    "tag": "sport",
    "count": 1,
    "articles": [
        "1"
    ],
    "related_tags": [
        "finance"
    ]
}

```

### Visualising Database Data
The Django administration portal can be used to view the database entries via an easy-to-use interface. To use this service, navigate to `http://localhost:8000/admin/` and use the credentials as defined in `DJANGO_SUPERUSER_USERNAME` and `DJANGO_SUPERUSER_PASSWORD`



### Tests

Tests can be run using the following `make` command
```
➜  make test
```