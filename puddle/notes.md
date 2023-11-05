# Step 1 --> Installations:

    - Install Virtual Enviourment (recomended)
    - Activated the venv
    - Install Django
    - Run the server to see if the istallation has worked

# Step 2 --> Django App:

    - Why do we need to create app?
        - It use to seperate different part of the website (models, views, urls, templates)
        - For Example: Home page, About page, Contact us page, etc will be in the same app
        - But, will have conversations in a different app
        - Similarly one app for items and so on
    - Create app by following commands:
        - python manage.py startapp (appname)

# Step 3 --> Working with the App:

    - In project file in `settings.py` file in installed app
    - Define the app name we've just created

# Step 3.1 --> Creating app's 1st view:

    - Handling the HTTP requests
    - Create a function for redering the templates
    - Render the Templates

# Step 3.2 --> Setting up the URLS:

    - Create folder named templates/(appname)/.html file
    - Create a urls file in the app folder and call the views set up the routs
    - Include the path in the main project urls file

# Step 4 --> Templates:

    - Create a base.html file
        - To cut out the unneccessary work
        - We need to have the menu/navbar and footer always be there in any pages
        - So, Its a good idea to have the base html.file
    - Extend the base.html file in all the pages
    - {% extends 'core/base.html %}
    - Add `{% block content %}, {% endblokc %} to render the content`

# Step 5 --> Creating a Seperate app for itesm:

    - Its always a good idea to have seperate apps for seperate things
    - Create a app for items
    - After creating the app
        - 1st thing to do is show the app to the django settings
    - Create models

# Step 5 --> Creating superuser for admin:

    - Create a super user for admin site
    - define the models (SQL)
    - To show the specific names and categories in the admin pannel
        - Define funciton to represents the stings
        - give names to categories
        - return the name

# Step 6 --> Images:

    - Django doesn't allow us to add directly
    - We need to install pillow
    - After that define the media folder in settings
    - And define the root of the images
