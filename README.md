## Start Project
1. Clone the repository
2. Create venv - python 3.11.5
4. Activate venv
5. pip install -r requirements.txt
6. copy .env.example to .env and fill in the fields
7. Create mysql schema "smartbeehive"

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```