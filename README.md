# djangoJWT
> Django JWT authentication system in backend development.

### Dependencies:
- python3.9
- Django 3.1.6
- psql (PostgreSQL) 12.5

The following steps will walk you thru installation on a Mac. Linux should be similar. It's also possible to develop on a Windows machine, but I have not documented the steps. If you've developed the Django app on Windows, you should have little problem getting up and running.

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
