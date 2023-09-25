18-1. New Projects
========================================================

To get a better idea of what Django does, build a couple of empty projects, like snap_gram or insta_chat.

* Make a new directory

```shell
mkdir snap_gram
```

* Create a virtual environment within this new directory. Using OS Monterey 12.7. There is no more Python2. 

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

* Create a new Django project called snapgram_project
```shell
django-admin startproject snapgram_project .
```

* Create the database
```shell
python manage.py migrate
```

* Run the Django development server
```shell
python manage.py runserver
```

* The install worked successfully! 
  
![Try It Yourself-18-1](https://github.com/nihathalici/Python-Crash-Course-The-Book/blob/main/Projects/Django-Project/2nd-Loop/00-Getting-started-with-Django/screenshots/screenshot_try_it_yourselr_18_1.PNG)
