This is a Django/Graphene GraphQL backend API by Rayton Lin at github.com/raytonlin1. It is started with the following commands.
    py -m venv venv
    venv\Scripts\activate
    pip install django
    django-admin startproject core .
    py manage.py startapp books
We make a new model in models.py called Books with a title and except.
We migrate the changes by using
    py manage.py makemigrations
    py manage.py migrate
Then we install Graphene using 
    pip install "graphene-django>=2.0"
and we add 'graphene_django' to settings.py.
Then we create schema.py in the books app, building a query using classes to get the fields in Books model that we want.
Then, we include
    path('books/', include('books.urls'))
in our urls.py in core, then create urls.py in books.
Also, make changes for Django 4.0 https://stackoverflow.com/questions/70382084/import-error-force-text-from-django-utils-encoding
Then, do py manage.py createsuperuser and include admin.site.register(Books) in admin.py.



