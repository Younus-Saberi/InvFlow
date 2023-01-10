# inventory management software
A simple inventory management system built with Django.
Users can add stock item and generate bills. All data is stored in database and are rendered in real time

To run project, run the following commands in the project's directory to create the database. When running the software for the first time, it is necessary to run each command for each app in the project

# Here are some screenshot of our application

<img src="res/landing-page.png">
<img src="res/admin-panel.png">
<img src="res/billing-page.png">

```
python manage.py makemigrations homepage
python manage.py migrate homepage
python manage.py makemigrations inventory
python manage.py migrate inventory
python manage.py makemigrations transactions
python manage.py migrate transactions
```
After the first time, the following can be run to migrate model changes in any app
```
python manage.py makemigrations
python manage.py migrate
```
Use the following command to run the server
```
python manage.py runserver
```
Use the following command to create an admin user 
```
python manage.py createsuperuser
```

To run Dockerfile use below commands

Build an image for the application

```
docker build -t invflow .
```

Run the image on loacl host

```
docker run -p 8000:8000 invflow
```
