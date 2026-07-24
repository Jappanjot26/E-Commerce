- virtualenv <name> : Create a Virtual Env
- source <virtualenv_name>/bin/activate : Start Virtual Env
- django-admin startproject <project_name> : creates a folder with initial django files

<!-- Example of files created initially -->
- <project_name>/
    - manage.py : Brain of project to talk to BE
    - <project_name>/
        - __init__.py
        - asgi.py : Server File
        - settings.py : Configuration for Project
        - urls.py : Table of contents of all pages in Project
        - wsgi.py : Server File

<!-- Always run after making changes to DB -->
- python manage.py makemigrations : To Create Migration whenever changed in DB
- python manage.py migrate : To include the migration to the DB (initially uses db.sqlite3)


- python manage.py createsuperuser : To create a super user from terminal (Created admin/1234)

<!-- Create a folder apps/ and sub-folder apps/core/ (python manage.py startapp core apps/core) -->
- python manage.py startapp <name> <place> : Create more file inside <place>

<!-- Example structure of files created -->
- <name>/
    - migrations/
        - __init__.py
    - __init__.py
    - admin.py
    - apps.py
    - models.py
    - tests.py
    - views.py

- Create a template folder inside core with a file as base.html and pasted content from github
- Create a frontpage.html in same folder which will extend base.html and paste some content in content block

- Added a function called frontpage which renders frontpage.html in `saulgadgets/apps/core/views.py`
- Imported this function in `saulgadgets/saulgadgets/urls.py` and added '' as path and a name for this template
- Added 'apps.core.apps.CoreConfig' in Installed apps in `saulgadgets/saulgadgets/settings.py` to tell that we have a app in it
- Changed from 'core' to 'apps.core' in `saulgadgets/apps/core/apps.py`

- python manage.py runserver : To start the server

<!-- To link a page/url -->
- add a link in <a> as href="{% url 'contact' %}



### TODO List
-Create a virtual environment
-Install Django and create a project
-Set up the database
-Create a superuser
-Create a folder for the Django apps
-Create folder and Django app for the core views (apps/core)
    -Create the base template
-Create view for the front page and a very basic template
-Creating a contact simple page
-Check that everything is working