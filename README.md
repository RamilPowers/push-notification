# Push-notifications service for smartphones with Django and Firebase
#### With this application you can make push-notifications to Android/iOS smartphones.

Description
-----------------------------------
1. All you need are device-token and app-token.  
2. The app uses `Pipenv`.

Installation
-----------------------------------
1. Copy the project with  
`git clone https://github.com/RamilPowers/push-notification.git .`
2. Activate the Pipenv virtual environment with  
`pipenv shell`
3. Install packets with  
`pipenv install`
4. Make migrations with  
`python manage.py makemigrations`
5. Apply migrations with  
`python manage.py migrate`
6. And finally you can run the project  
`python manage.py runserver`