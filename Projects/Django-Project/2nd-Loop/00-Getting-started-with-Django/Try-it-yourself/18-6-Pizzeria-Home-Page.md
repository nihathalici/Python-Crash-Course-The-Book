18-6. Pizzeria Home Page
========================================================

Add a home page to the Pizzeria project you started in Exercise 18-4. 

* **[18.4. Pizzeria](https://github.com/nihathalici/Python-Crash-Course-The-Book/blob/main/Projects/Django-Project/2nd-Loop/00-Getting-started-with-Django/Try-it-yourself/18-4-Pizzeria.md)** - Here, we've started a new project called pizzeria with an app called pizzas.

* Edit the urls.py files. First the project urls file.
```python
# pizzeria_project/urls.py

from django.contrib import admin
from django.urls import path, include #new

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pizzas.urls")), #new
]
```

* Now create a urls.py file in pizzas dictionary:
```python
# pizzas/urls.py
"""Defines URL patterns for pizzas."""

from django.urls import path
from . import views

app_name = "pizzas"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
]
```

* Write the view:
```python
# pizzas/views.py

from django.shortcuts import render

def index(request):
    return render(request, "pizzas/index.html")
```

* Inside the pizzeria folder, make a new folder called templates. Inside the templates folder, make another folder called pizzas.
Inside the inner pizzas folder, make a new file called index.html.

```html
<!-- pizzas/templates/pizzas/index.html -->
<p>Porta a Napoli</p>

<p>Get ready to savor the perfect slice!</p> 

<p>Our mouthwatering pizza paradise is under construction and coming soon to satisfy your cravings.</p>
```

* Run the Django development server
```shell
python manage.py runserver
```

![Try It Yourself-18-6](https://github.com/nihathalici/Python-Crash-Course-The-Book/blob/main/Projects/Django-Project/2nd-Loop/00-Getting-started-with-Django/screenshots/screenshot_try_it_yourself_18_6_pizzeria_Home_Page.PNG)
