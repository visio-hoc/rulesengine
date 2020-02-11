# Visio Lending RulesEngine Coding Test

This test was done in Python 3.7 using the [Django Framework](https://www.djangoproject.com/) 

## Installation

Create a local folder and clone the repo

```sh
$ mkdir RulesEngine
$ cd RulesEngine
$ git clone this repo
```

Note if you don't have pip3 or python3-venv then you have to install those first:

```sh
$ sudo apt install python3-pip
$ sudo apt-get install python3-venv
```

Please use the python `virtualenv` tool to build locally:

```sh
$ pip3 install virtualenv
$ python3 -m venv venv
$ source venv/bin/activate
$ cd RulesEngine
$ pip3 install -r requirements.txt
$ python3 manage.py runserver
```

Then visit `http://localhost:8000` to view the app.

If you are using a remote server run this command instead:

```sh
$ python3 manage.py runserver 0.0.0.0:8000
```

You also have to check that port 8000 (or whatever port you used) is open.
Then you need to edit the rulesengine/visio/settings.py file and change

```
ALLOWED_HOSTS = ['my_server_ip_or_dns_name']
```

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
