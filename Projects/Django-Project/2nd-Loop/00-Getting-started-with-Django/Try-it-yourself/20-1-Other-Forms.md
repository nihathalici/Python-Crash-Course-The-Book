20-1. Other Forms
========================================================

We applied Bootstrap’s styles to the login page. Make similar changes to the rest of the form-based pages including new_topic, new_entry, edit_entry, and register.

* new_topic:
```html
{% extends 'learning_logs/base.html' %}
{% load bootstrap4 %}

{% block page_header %}
<h2>Add a new topic:</h2>    
{% endblock page_header %}
    
{% block content %}
<form action="{% url 'learning_logs:new_topic' %}" method="post" class="form">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
    <button name="submit" class="btn btn-primary">Add topic</button>
    {% endbuttons %}
    <input type="hidden" name="next" value="{% url 'learning_logs:topics_list' %}">
</form>
    
{% endblock content %}   
```
![Try It Yourself-20-1 - 1](https://github.com/nihathalici/Python-Crash-Course-The-Book/blob/main/Projects/Django-Project/2nd-Loop/00-Getting-started-with-Django/screenshots/screenshot_try_it_yourself_20_1_new_topic.PNG)

new_entry:
```html
{% extends 'learning_logs/base.html' %}
{% load bootstrap4 %}

{% block page_header %}
<h2>Add a new entry:</h2>  
<h2><a href="{% url 'learning_logs:topics_detail' topic.id %}">{{ topic }}</a></h2>
{% endblock page_header %}
    
{% block content %}
<form action="{% url 'learning_logs:new_entry' topic.id %}" method="post" class="form">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% buttons %}
    <button name="submit" class="btn btn-primary">Add entry</button>
    {% endbuttons %}
</form>   
{% endblock content %}  
```
![Try It Yourself-20-1 - 2](https://github.com/nihathalici/Python-Crash-Course-The-Book/blob/main/Projects/Django-Project/2nd-Loop/00-Getting-started-with-Django/screenshots/screenshot_try_it_yourself_20_1_new_entry.PNG)

