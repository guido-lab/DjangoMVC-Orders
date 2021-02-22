# DjangoMVC-Orders

## Coding tasks:
A MVC Demo application:
- Please design a model where we have entities: User, Order and Order items (with appropriate relations defined)
- Prepare a simple form which will save data of an Order to a database (please also use some form validations)
- Create a page which will list all the OrdersRecommendations:
- Usage of ORM layer is highly encouraged

## How to setup:
Clone This Project (Make Sure You Have Git Installed)
```
https://github.com/guido-lab/DjangoMVC-Orders.git
```

The following command creates a new virtual environment named venv in the current directory:

```bash
$ python -m venv env
```

Activate virtual environment:

```bash
(Mac/Linux) $ source env/bin/activate
```

```bash
(Windows) $ source env/Scripts/activate
```

Install Dependencies:

```
$ pip install -r requirements.txt
```

Set Database (Make Sure you are in the same directory as manage.py):
```
$ python manage.py makemigrations
$ python manage.py migrate
```
Create SuperUser:
```
$ python manage.py createsuperuser
```

Run the development server:

```bash
$ python manage.py runserver
```

The project is runing at: **http://127.0.0.1:8000/**

Access admin pannel: **http://127.0.0.1:8000/admin**
