# django-coin-api
Rest ful API with Django

# Installation

1. Clone project. 
```bash
git clone https://github.com/antoniogmzstat/django-coin-api.git
```

2. Create virtual env for install packages
```bash
python -m virtualenv venv
```

3. Activate virtual env
```bash
source ./venv/bin/activate
```

4. Install list of packages from file requeriments.txt
```bash
pip install -r requirements.txt
```

5. Make migrations for the application

```bash
python manage.py makemigrations coins
```
```bash
python manage.py migrate
```

6. Copy csv files with data into folder "data"

7. Create table into SQLite
```bash
python manage.py runscript load
```

8. Up Server
```bash
python manage.py runserver
```

9. Access to http://127.0.0.1:8000/api/v.1.0/