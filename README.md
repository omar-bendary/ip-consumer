# IP Consumer API

This Django project provides endpoints for consuming IP addresses, validating them, and updating their information asynchronously. Additionally, it implements WebSocket functionality for real-time updates of IP information. By following the structure and components outlined in this documentation, clinte-side can effectively understand and use the functionality of the project.

# Getting started

## Installation

make a new folder for the project and open this folder in the Terminal/Windows (PowerShell) and run this command

```bash
git clone https://github.com/omar-bendary/ip-consumer.git
```

# Pre-requisites and Local Development

# Using Docker and Docker compose

The first step is to sign up for
a free account on [DockerHub](https://hub.docker.com/signup)  and then install the Docker desktop app on your local machine:

* [Docker for Mac](https://docs.docker.com/desktop/install/mac-install/)
* [Docker for Windows](https://docs.docker.com/desktop/install/windows-install/)
  Once Docker is done installing we can confirm the correct version is running by typing the
  command docker --version in the command line shell

```shell
$ docker --version
Docker version 20.10.14, build a224086
```

### Set up your RDBMS , open your setting.py

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "postgres",
        "HOST": "db",  # set in docker-compose.yml
        "PORT": 5432,  # default postgres port
    }
}
```

<br/>
 All the extracted IP data is saved to the database to use it later if needed.
<br/>
<br/>

### Running our container

1- Open the project Code folder in Terminal/Windows (PowerShell).

2- Run this command .

```bash
docker-compose up -d --build
```

### To Stop the currently running container

Control+c (press the “Control” and “c” button at
the same time) and additionally type docker-compose down.

```shell
docker-compose down
```

### Now let’s confirm everything is working

```bash
docker-compose exec web python manage.py  makemigrations 
```

```bash
docker-compose exec web python manage.py  migrate 
```

> Now create the admin user

```bash
 docker-compose exec web python manage.py createsuperuser 
```

The application is run on http://127.0.0.1:8000/

# Using virtual environment approach.

## To create a virtual environment

Make Sure that [Redis](https://redis.io/docs/install/) is up and running

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install packages.

1- Open the project Code folder in Terminal/Windows (PowerShell).

2- Run this command .

```bash
# Windows
> python -m venv .venv
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# macOS
% python3 -m venv .venv
```

### To activate a new virtual environment called .venv:

```bash
# Windows
> .venv\Scripts\Activate.ps1
(.venv) >

# macOS
% source .venv/bin/activate
(.venv) %
```

### To deactivate and leave a virtual environment type deactivate.

```bash
# Windows
(.venv) > deactivate
>

# macOS
(.venv) % deactivate
%
```

### install requirements.txt

Run `pip install requirements.txt`. All required packages are included in the requirements file.

> make sure to activate the virtual environment first

```bash
pip install -r requirements.txt
```

**You might see a WARNING message about updating pip after running these commands. It’s always good to be on the latest version of software and to remove the annoying WARNING message each time you use pip. You can either copy and paste the recommended command or run `python -m pip install --upgrade pip` to be on the latest version.**

```bash
(.venv) > python -m pip install --upgrade pip
```

## Now let’s confirm everything is working by running Django’s internal web server via the runserver command

```bash
(.venv) > python manage.py  makemigrations 
```

```bash
(.venv) > python manage.py  migrate 
```

> Now create the admin user

```bash
(.venv) > python manage.py createsuperuser 
```

Run the surver

```bash
# Windows
(.venv) > python manage.py runserver

# macOS
(.venv) % python3 manage.py runserver
```

## Set up your RDBMS , open your setting.py

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_project_name',
        'USER': 'your_postgres_username',
        'PASSWORD': 'your_postgres_password',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '5432',
    }
}
```

Or you can stick the default database (sqlite3) but not recommended for Production.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

<br/>
All the extracted IP data is saved to the database to use it later if needed.
<br/>
The application is run on http://127.0.0.1:8000/ by default in the backend configuration.

## Endpoints

The backend server offers the following endpoints:

* **POST /ip-consumer** : Accepts a list of IP addresses and adds them to the database for further processing.
* **WebSocket /ws/ip_details/** : Provides real-time updates on IP address details.

## Usage Instructions

### 1. Adding IP Addresses

Endpoint

* **POST api//ip-consumer**

Request Format

```json
{
  "ip_addresses": ["192.168.0.1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"]
}
```

Description

* Send a POST request to the `/api/ip-consumer` endpoint with a JSON payload containing a list of IP addresses.
* The server validates each IP address, adds it to the database if valid, and triggers an asynchronous task to update its information.

#### Example Request (cURL)

```bash
curl -X POST http://127.0.0.1:8000/api/ip-consumer
    -H "Content-Type: application/json"
    -d '{"ip_addresses": ["192.168.0.1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"]}'
```



### 2. Real-time IP Details Updates

WebSocket Endpoint

* **WebSocket /ws/ip_details/**

#### Description

* Connect to the WebSocket endpoint `/ws/ip_details/` to receive real-time updates on IP address details.
* Once connected, the server will push updates whenever new information becomes available for any IP address.

#### Example JavaScript Connection

```javascript
const socket = new WebSocket('ws://127.0.0.1:8000/ws/ip_details/');

socket.onopen = function(event) {
  console.log('WebSocket connection established.');
};

socket.onmessage = function(event) {
  const data = JSON.parse(event.data);
  console.log('Received IP details update:', data);
};

socket.onclose = function(event) {
  console.log('WebSocket connection closed.');
};

socket.onerror = function(error) {
  console.error('WebSocket error:', error);
};

```
