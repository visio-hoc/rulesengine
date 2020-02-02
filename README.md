# Visio Lending RulesEngine Coding Test

This test was done in Python 3.7 using the [Django Framework](https://www.djangoproject.com/) 

## Installation

Create a local folder and clone the repo

```sh
$ mkdir RulesEngine
$ cd RulesEngine
$ git clone this repo
```

Please use the python `virtualenv` tool to build locally:

```sh
$ pip install virtualenv
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ python3 manage.py runserver
```

Then visit `http://localhost:8000` to view the app.

Note on Windows, the commands will be slightly different:

```sh
$ pip install virtualenv
$ python -m venv venv
$ call venv/Scripts/activate
$ pip install -r requirements.txt
$ python manage.py runserver
```

## Testing

```sh
$ python3 manage.py test
```
