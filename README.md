# django-coin-api
Rest ful API with Django

# Installation

1. Clone project. 
```bash
git clone https://github.com/antoniogmzstat/django-coin-api.git
```

2. Situate into project folder

```bash
cd ./django-coin-api/
```

3. Create virtual env for install packages
```bash
python -m virtualenv venv
```

4. Activate virtual env
```bash
source ./venv/bin/activate
```

5. Install list of packages from file requeriments.txt
```bash
pip install -r requirements.txt
```

6. Make migrations for the application

```bash
python manage.py makemigrations coins
```
```bash
python manage.py migrate
```

7. Create folder with name: "data" in path django-coin-api/scripts and copy csv files with data into the new folder "data"

django-coin-api/scripts
- load.py
- data:
    * coin_Aave.csv
    * etc.


8. Create table into SQLite
```bash
python manage.py runscript load
```

9. Set Up Server
```bash
python manage.py runserver
```

10. Access to http://127.0.0.1:8000/api/v.1.0/