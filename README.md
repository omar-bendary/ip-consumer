# IP Consumer API

# IP Consumer API

This Django project provides endpoints for consuming IP addresses, validating them, and updating their information asynchronously. Additionally, it implements WebSocket functionality for real-time updates of IP information. By following the structure and components outlined in this documentation, clients can effectively understand and use the functionality of the project.

---

## **Access Control and Database Usage**

In this project, everyone can access the socket, primarily for testing purposes. However, in a real-world scenario, it's crucial to implement permission controls to restrict access to specific sockets based on business requirements. For instance, users should only see their own sockets, or access could be limited to specific groups of people depending on business needs.

Regarding the database usage, while it's optional for this project, I've implemented a simple database to track IDs and their information for recording purposes. This setup allows us to extend the database functionality later if needed.

## **Getting started**

### **Installation**

To install the project, follow these steps:

1. Make a new folder for the project and open this folder in the Terminal/Windows PowerShell.
2. Run the following command to clone the project from GitHub:

```bash
git clone https://github.com/omar-bendary/ip-consumer.git
```

### **Create your .env file**

Create a **`.env`** file in the root directory of the project with the following environment variables:

```
plaintextCopy code
# ----------PostgreSQL------------------
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

#________Redis___________
REDIS_HOST=redis
REDIS_PORT=6379

#---IP Info Api -----------
API_TOKEN=your_api_token

Save to grepper

```

## **Pre-requisites and Local Development**

# **Using Docker and Docker Compose**

To run the project using Docker and Docker Compose:

1. Sign up for a free account on [DockerHub](https://hub.docker.com/signup) and install the Docker desktop app on your local machine.
2. Confirm Docker installation by running **`docker --version`** in the command line shell.

```
$ docker --version
Docker version 20.10.14, build a224086
```

### Set up your RDBMS

Open your **`settings.py`** file and configure your PostgreSQL database settings:

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

### **Running Docker Containers**

To start the containers:

1. Open the project folder in the Terminal/Windows PowerShell.
2. Run the following command:

```bash
docker-compose up -d --build
```

To stop the containers, use **`docker-compose down`**.

### Note:

- All extracted IP data is saved to the database for future reference.
- The application runs on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) by default.

# **Using Virtual Environment**

To run the project using a virtual environment:

1. Ensure Redis is installed and running.
2. Navigate to the project folder in Terminal/Windows PowerShell.
3. Create a virtual environment and activate it:

```bash
# Windows
> python -m venv .venv
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# macOS
% python3 -m venv .venv

```

Activate the virtual environment:

```bash
# Windows
> .venv\Scripts\Activate.ps1
(.venv) >

# macOS
% source .venv/bin/activate
(.venv) %
```

Install requirements:

```bash
pip install -r requirements.txt
```

### Set up your RDBMS

Configure your database settings in **`[settings.py](http://settings.py)` as before**.

### Run the Development Server

```bash
# Windows
(.venv) > python manage.py runserver

# macOS
(.venv) % python3 manage.py runserver
```

### Run the Celery Worker

```bash
celery -A config worker --loglevel=info
```

### Note:

- All extracted IP data is saved to the database for future reference.
- The application runs on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) by default.

# **Endpoints**

The backend server offers the following endpoints:

- **POST /api/ip-consumer**: Accepts a list of IP addresses and adds them to the database for further processing.
- **WebSocket /ws/ip_details/**: Provides real-time updates on IP address details.

## **Usage Instructions**

### **1. Adding IP Addresses**

**Endpoint:**

- **POST /api/ip-consumer**

**Request Format:**

```json
{
  "ip_addresses": ["192.168.0.1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"]
}
```

**Description:**

- Send a POST request to the **`/api/ip-consumer`** endpoint with a JSON payload containing a list of IP addresses.
- The server validates each IP address, adds it to the database if valid, and triggers an asynchronous task to update its information.

**Example Request (cURL):**

```bash
curl -X POST http://127.0.0.1:8000/api/ip-consumer \
    -H "Content-Type: application/json" \
    -d '{"ip_addresses": ["192.168.0.1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"]}'

```

### **2. Real-time IP Details Updates**

**WebSocket Endpoint:**

- **WebSocket /ws/ip_details/**

**Description:**

- Connect to the WebSocket endpoint **`/ws/ip_details/`** to receive real-time updates on IP address details.
- Once connected, the server will push updates whenever new information becomes available for any IP address.

**Example JavaScript Connection:**

```jsx
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

This Django project provides endpoints for consuming IP addresses, validating them, and updating their information asynchronously. Additionally, it implements WebSocket functionality for real-time updates of IP information. By following the structure and components outlined in this documentation, clients can effectively understand and use the functionality of the project.

---

## **Access Control and Database Usage**

In this project, everyone can access the socket, primarily for testing purposes. However, in a real-world scenario, it's crucial to implement permission controls to restrict access to specific sockets based on business requirements. For instance, users should only see their own sockets, or access could be limited to specific groups of people depending on business needs.

Regarding the database usage, while it's optional for this project, I've implemented a simple database to track IDs and their information for recording purposes. This setup allows us to extend the database functionality later if needed.

## **Getting started**

### **Installation**

To install the project, follow these steps:

1. Make a new folder for the project and open this folder in the Terminal/Windows PowerShell.
2. Run the following command to clone the project from GitHub:

```bash
git clone https://github.com/omar-bendary/ip-consumer.git
```

### **Create your .env file**

Create a **`.env`** file in the root directory of the project with the following environment variables:

```
# ----------PostgreSQL------------------
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres

#________Redis___________
REDIS_HOST=redis
REDIS_PORT=6379

#---IP Info Api -----------
API_TOKEN=your_api_token


```

## **Pre-requisites and Local Development**

## **Using Docker and Docker Compose**

To run the project using Docker and Docker Compose:

1. Sign up for a free account on [DockerHub](https://hub.docker.com/signup) and install the Docker desktop app on your local machine.
2. Confirm Docker installation by running **`docker --version`** in the command line shell.

```
$ docker --version
Docker version 20.10.14, build a224086
```

### Set up your RDBMS

Open your **`settings.py`** file and configure your PostgreSQL database settings:

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

### **Running Docker Containers**

To start the containers:

1. Open the project folder in the Terminal/Windows PowerShell.
2. Run the following command:

```bash
docker-compose up -d --build
```

To stop the containers, use **`docker-compose down`**.

### Note:

- All extracted IP data is saved to the database for future reference.
- The application runs on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) by default.

## **Using Virtual Environment**

To run the project using a virtual environment:

1. Ensure Redis is installed and running.
2. Navigate to the project folder in Terminal/Windows PowerShell.
3. Create a virtual environment and activate it:

```bash
# Windows
> python -m venv .venv
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# macOS
% python3 -m venv .venv

```

Activate the virtual environment:

```bash
# Windows
> .venv\Scripts\Activate.ps1
(.venv) >

# macOS
% source .venv/bin/activate
(.venv) %
```

Install requirements:

```bash
pip install -r requirements.txt
```

### Set up your RDBMS

Configure your database settings in **`settings.py` as before**.

### Run the Development Server

```bash
# Windows
(.venv) > python manage.py runserver

# macOS
(.venv) % python3 manage.py runserver
```

### Note:

- All extracted IP data is saved to the database for future reference.
- The application runs on [http://127.0.0.1:8000/](http://127.0.0.1:8000/) by default.

## **Endpoints**

The backend server offers the following endpoints:

- **POST /api/ip-consumer**: Accepts a list of IP addresses and adds them to the database for further processing.
- **WebSocket /ws/ip_details/**: Provides real-time updates on IP address details.

## **Usage Instructions**

### **1. Adding IP Addresses**

**Endpoint:**

- **POST /api/ip-consumer**

**Request Format:**

```json
{
  "ip_addresses": ["192.168.0.1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"]
}
```

**Description:**

- Send a POST request to the **`/api/ip-consumer`** endpoint with a JSON payload containing a list of IP addresses.
- The server validates each IP address, adds it to the database if valid, and triggers an asynchronous task to update its information.

**Example Request (cURL):**

```bash
curl -X POST http://127.0.0.1:8000/api/ip-consumer \
    -H "Content-Type: application/json" \
    -d '{"ip_addresses": ["192.168.0.1", "2001:0db8:85a3:0000:0000:8a2e:0370:7334"]}'

```

### **2. Real-time IP Details Updates**

**WebSocket Endpoint:**

- **WebSocket /ws/ip_details/**

**Description:**

- Connect to the WebSocket endpoint **`/ws/ip_details/`** to receive real-time updates on IP address details.
- Once connected, the server will push updates whenever new information becomes available for any IP address.

**Example JavaScript Connection:**

```jsx
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
