## Event Management System 

Event management system for keeping records of user events. Contains the type of event, its date and time, information about the event. To work with the system, the user must be registered and authenticated.

For user authentication was used rest_framework.authtoken. You can also add djoser library to extend the functionality of working with the User model.

If the incoming event name is not in the database, then create it. All event names are stored in the lower register to prevent data duplication.

Create event post request covered by Test Cases

## Tech details

|**Resource**|**Resource Name**|**Version**|
| :-: | :-: | :-: | 
|Back-end programming language|Python|3.10.5|
|Back-end web framework|Django|4.1.6|
|REST APIs toolkit|Django Rest Framework|3.14.0|
|Database|SQLite|3.12.2|
|Web server|||

## Installation & Lunch

How to run a project locally?

1. Preparing

```sh
pip install pipenv
pipenv shell
pipenv install
```

2. Start server

```sh
python manage.py runserver
```

3. Stop server

```sh
Ctrl+C
```

4. Run migrations or database schema 
```sh
./manage.py migrate
```
5. Run unit tests 

```sh
./manage.py test
```

## Managing environment variables

Add some exports to your shell profile `~/.zshrc` or `~/.bashrc`<br>
Or paste these variables into `.env` file inside the project (without **export**)

```sh
export ENVIRONMENT = local    # environments keys (prod, local)

export SECRET_KEY=some_key

export DB_NAME = your_db_name
export ALLOWED_HOSTS = your_allowed_hosts []
export STATIC_URL = 'static/'
```

Restart your terminal for changes to take effect.
