# Bitbucket Webhook

## Running procedure
1. Create a file .env in the root directory and specify the following variables:
	- `DEBUG` - enable DEBUG mode
	- `AGENT_HOST` - if not DEBUG, then specify the address which will be assigned to the app (it is passed to Django's `ALLOWED_HOSTS`
	- `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASSWORD`, `DB_NAME` - credentials of a running instance of Postgres. Default values are `localhost`, `5432`, `postgres`, `123456`, `postrgres` respectively.
	- `SECRET_KEY` - Django's secret key. Must be specified if not DEBUG
2. `docker-compose up`

## Integration
The application creates 2 tables at `postgres/public`: `bitbucket_agent_report` and `django_migrations`. The first one contains the actual information from BitBucket, and the second one is for service purposes.

The columns in `bitbucket_agent_report` are the following:
- `id` *(Integer)* -- Primary key
- `eventKey` *(Text)* -- The event tag. See in [official documentation](https://confluence.atlassian.com/bitbucketserver070/event-payload-996644369.html#Eventpayload-repositoryevents).
- `date` *(Timestamp with time zone)* -- the timestamp of the event specified by Bitbucket
- `actor` *(Text)* -- A JSON string describing an actor. Example:
    ```
    {
        'name': 'mavl', 
        'emailAddress': 'AAAAAA@AAAAAA.com', 
        'id': 1, 
        'displayName': 'Mavl', 
        'active': True, 
        'slug': 'mavl', 
        'type': 'NORMAL', 
        'links': {
                'self': [{'href': 'http://10.90.138.181:7990/users/mavl'}]
                }
    }
    ```
- `raw` *(Text)* -- The RAW unformatted data received from the Bitbucket. Needed for deserialization and for HMAC calculation.
- `received_on` *(Timestamp with time zone)* -- the timestamp when this event has been received by the agent 
- `HMAC` *(Text)* -- HMAC checksum received from Bitbucket. This value is a **HMAC SHA256 (with specified secret key)** checksum calculated on the RAW data as a whole.
