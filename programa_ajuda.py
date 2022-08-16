from os import system

system("virtualenv venv")
system("venv\scripts\activate")
system("pip install django")
system("python manage.py runserver")

