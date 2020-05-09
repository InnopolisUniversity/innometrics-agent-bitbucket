# Bitbucket Webhook

## Running procedure
1. Create a file .env in the root directory and specify the following variables:
	- `DEBUG` - enable DEBUG mode
	- `AGENT_HOST` - if not DEBUG, then specify the address which will be assigned to the app (it is passed to Django's `ALLOWED_HOSTS`
	- `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` - credentials of a running instance of Postgres. Default values are `localhost`, `5432`, `postgres`, `123456`, `postrgres` respectively.
	- `SECRET_KEY` - Django's secret key. Must be specified if not DEBUG
2. `docker-compose up`