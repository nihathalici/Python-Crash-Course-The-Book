
18-8. Pizzeria Pages
========================================================

Add a page to the Pizzeria project that shows the names of available pizzas. Then link each pizza name to a page displaying the pizza’s toppings. Make sure you use template inheritance to build your pages efficiently.
 
* Create a parent template: base.html
```html
<!-- pizzas/templates/pizzas/base.html -->
<p>
<a href="{% url 'pizzas:index' %}">Porta a Napoli</a>
</p>

{% block content %}
    
{% endblock content %}
```

* Modify the index.html
```html
<!-- pizzas/templates/pizzas/index.html -->
{% extends 'pizzas/base.html' %}

{% block content %}
<p>Get ready to savor the perfect slice!</p> 

<p>Our mouthwatering pizza paradise is under construction and coming soon to satisfy your cravings.</p>    
{% endblock content %}
```

* Start to build the pizzas_list page with adding the URL path.
```python
"""Defines URL patterns for pizzas."""

from django.urls import path
from . import views

app_name = "pizzas"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
    # Page that shows all pizzas
    path("pizzas_list/", views.pizzas_list, name="pizzas_list"), #new
]
```

* Now add the associated pizzas_list function to the views.py
```python
# pizzas/views.py

from django.shortcuts import render

from .models import Pizza # new

def index(request):
    return render(request, "pizzas/index.html")

def pizzas_list(request): # new
    """Show all pizzas."""
    pizzas_list = Pizza.objects.all()
    context = {"pizzas_list": pizzas_list}
    return render(request, "pizzas/pizzas_list.html", context)
    
```

* The template for the pizzas_list page   
```html
<!-- pizzas/templates/pizzas/pizzas_list.html -->
{% extends 'pizzas/base.html' %}

{% block content %}
<p>Pizzas</p>
<ul>
  
  {% for pizza in pizzas_list %}
    <li>{{ pizza }}</li>
  {% empty %}
    <li>No pizzas have been added yet.</li>
  {% endfor %}
</ul>
{% endblock content %} 
```

* Include the new page to the base.html 
```html
<p>
<a href="{% url 'pizzas:index' %}">Porta a Napoli</a>
<a href="{% url 'pizzas:pizzas_list' %}">Our Pizzas</a> # new
</p>

{% block content %}
    
{% endblock content %}
    
```

* Run the Django development server
```shell
python manage.py runserver
```

* It works!
![Try It Yourself-18-8 - 1](https://github.com/nihathalici/Python-Crash-Course-The-Book/blob/main/Projects/Django-Project/2nd-Loop/00-Getting-started-with-Django/screenshots/screenshot_try_it_yourself_18_8_pizzeria_Adding_Pages.PNG)
