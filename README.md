## Event Management System 

Event management system for keeping records of user events. 
Contains the type of event, its date and time, information about the event. 
To work with the system, the user must be registered and authenticated.

### Authentication

For user authentication was used rest_framework.authtoken. 
You can also add djoser library to extend the functionality of working with the User model.

### List of events

System has list of user's events, with filtering by event_type name and timestamp date and time range. 
The system also includes an endpoint with list of all existing event names.

### Create event functionality

When the user create the event, if the event's name isn't in the database, system add it automatically. 
All event names are stored in the lower register to prevent data duplication.

### Admin Panel

Add Django admin panel with models Event and EventType. For the Event model, add filtering by event_type name and timestamp datetime range.

### API Test Cases

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
```

Restart your terminal for changes to take effect.

### Documentation

Project has swagger autodocumentation with permission class AllowAny. This is the way how another developers can see all endpoints of the project.
```sh
BACK_END_DOMAIN_URL/api/v1.0/swagger/
```