# Django-JWT App
> Django JWT authentication system in backend development.

### Prerequisites:
- python 3.9
- Django 3.1.6
- psql (PostgreSQL) 12.5

The following steps will walk you thru installation on a Mac. I think Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed the `Django` app on Windows, you should have little problem getting up and running.

###### If psql error raise please follow the command.
```base 
pip install psycopg2-binary
```

If you contribute anything 1st setup and run the project in your local development server. Please follow the instructions.
```base
git clone https://github.com/mbrsagor/djangoJWT.git
cd djangoJWT
virtualenv venv --python=python3.9
source venv/bin/activate
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

N:B: Must be you have to change database name, username etc, otherwise you will got an error.
#### Example:
- Goto config folder
 - db_config.py change on your database user
- Follow the instruction

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_user_password',
        'HOST': 'localhost', # IP
        'PORT': '', # Port if available
    }
}
```
