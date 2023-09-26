18-4. Project Pizzeria
========================================================

Start a new project called pizzeria with an app called pizzas.

* Make a new directory

```shell
mkdir pizzeria
```

* Create a virtual environment within this new directory. 

```shell
python -m venv .venv
```

* Activate the virtual environment called .venv
```shell
source .venv/bin/activate
```

* Install Django
```shell
pip install django
```

* Create a new Django project called pizzeria_project. Don't forget to add the period (or dot) . at the end!
```shell
django-admin startproject pizzeria_project .
```

* Create the database
```shell
python manage.py migrate
```

* Run the Django development server
```shell
python manage.py runserver
```

* Create the app pizzas
```shell
python manage.py startapp pizzas
```

* Define the models
```python3

"""
Define a model Pizza with a field called name, which will 
hold name values, such as Hawaiian and Meat Lovers. 
Define a model called Topping with fields called 
pizza and name. The pizza field should be a foreign key 
to Pizza, and name should be able to hold values 
such as pineapple, Canadian bacon, and sausage.
"""

from django.db import models

class Pizza(models.Model):
    """Varieties, defined by the choice of toppings and crust."""
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name



class Topping(models.Model):
    """Any of the ingredients added over the pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name


```

* Modify settings.py and your app

```python3
INSTALLED_APPS = [
    # My apps
    "pizzas",
    # Default django apps.
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

* Add changes to database
```shell
python manage.py makemigrations pizzas
python manage.py migrate
```

* Set up a superuser
```shell
python manage.py createsuperuser
```

* Register the model with the admin site
```python3
from django.contrib import admin

from .models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)
```

* Use the superuser account to access the admin site

* Use the site to enter some pizza names and toppings. 

* Use the shell to explore the data you entered.
```shell
python manage.py shell
from pizzas.models import Pizza

Pizza.objects.all()

pizzas = Pizza.objects.all()
for pizza in pizzas:
  print(pizza.id, pizza)

p = Pizza.objects.get(id=1)
p.name

# Check the ForeignKey
p.topping_set.all()
p.topping_set.get(id=1)
```
