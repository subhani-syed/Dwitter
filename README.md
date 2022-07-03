# Dwitter
Simple Twitter Clone made using Django <a href = "https://twitter.com/subhan1syed" target="_blank"><img src="https://img.icons8.com/fluent/48/000000/twitter.png"/></a> <a href="https://www.djangoproject.com/"><img src="https://img.icons8.com/ios/50/undefined/django.png"/></a>

# Steps To Run Locally and Make Changes
The following command are meant to run in a terminal or cmd
### First create a directory
    mkdir <dir_name>
### Change into to directory
    cd <dir_name>
### Clone this Repo to the present directory
    git clone https://github.com/subhani-syed/Dwitter.git .
### Create a Virtual Environment
    python3 -m venv <env_name>
### Activate the Virtual Environment
    source <env_name>/bin/activate
### Install the required Dependencies using PIP
    pip install -r requirements.txt
### Make Migrations and Migrate To Create The Tables
    python3 manage.py makemigrations
    python3 manage.py migrate
### Create a Super User to Access the Admin Site
    python3 manage.py createsuperuser
### Run the Local Server on a specific Port
    python3 manage.py runserver PORT_NO
- By Default it runs on **127.0.0.1:8000**
- Now you can make changes to the project **[Refer this](https://github.com/subhani-syed/Dwitter/blob/main/CONTRIBUTING.md)**
### To Exit the Virtual Environment
    deactivate
    
If You find this project usefull giving it a  :star2: would be much appreciated. :blush:
