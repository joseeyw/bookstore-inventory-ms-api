# bookstore-inventory-ms-api
Bookstore Inventory Management System

## Setting up
### 1. Database

```diff
sudo -u postgres -i psql
```
```
CREATE DATABASE bookstore;
```
```
CREATE ROLE bookstore WITH PASSWORD 'bookstore';
```
```
GRANT ALL PRIVILEGES ON bookstore TO bookstore;

```
```
ALTER ROLE bookstore WITH LOGIN;
```
```
ALTER ROLE bookstore WITH CREATEDB;
```


### 2. Installing Dependencies
```diff 

+ python version  > 3.8
```
```
python3 -m venv .venv

```
```
source .venv/bin/activate
```
```
pip install -r requirements.txt
```
## Running the project
```
cd bookstore
```

#### configurations
```
cp bookstore/.env.example  bookstore/.env
```
### 1. setting up migrations
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```
### 2. Starting the api
```
python3 manage.py runserver
```
#### Access the API documentation on 
##### For the protected apis add authorization in format
```
Token tokengeneratedfromlogin
```
```
http://localhost:8000/swagger
```
### 3.Running tests
```
python3 manage.py test
```
