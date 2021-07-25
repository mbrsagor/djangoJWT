# Django-JWT App
> Django JWT authentication system in backend development.

### Prerequisites:
- python 3.9
- Django 3.1.6
- psql (PostgreSQL) 12.5

The following steps will walk you thru installation on a Mac. I think Linux should be similar, It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed the `Django` app on Windows, you should have little problem getting up and running.

###### If psql error raise please follow the command.
```base 
pip install psycopg2-binary
```

If you contribute anything 1st setup and run the project in your local development server. Please follow the instructions.
```base
git clone https://github.com/mbrsagor/djangoJWT.git
cd djangoJWT
virtualenv venv --python=python3.8
source venv/bin/activate
```

Then copy `.sample.env` and make `.env` file then paste the all codes:

```base
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```

#### Example `.env` files:

```.env
SECRET_KEY=SECRET_KEY
DEBUG=True
ALLOWED_HOSTS=*

# for localhost use
DB_HOST=localhost
DB_PORT=5432
DB_NAME=db_name
DB_USERNAME=db_user
DB_PASSWORD=db_password

EMAIL_HOST='mail.domain.com'
EMAIL_HOST_USER='abc@domain.com'
EMAIL_HOST_PASSWORD='abcdef'
DEFAULT_FROM_EMAIL='abc@domain.com'
SERVER_EMAIL='abc@domain.com'
EMAIL_PORT=25
EMAIL_USE_TLS=False
```
N:B: Must be you have to change database name, username etc, otherwise you will got an error.
