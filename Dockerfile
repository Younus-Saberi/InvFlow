FROM python:3.8

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt


RUN python manage.py makemigrations inventory && python manage.py migrate inventory
RUN python manage.py makemigrations transactions && python manage.py migrate transactions
RUN python manage.py makemigrations ; python manage.py migrate
EXPOSE 8000

CMD ["python", "manage.py", "runserver","0.0.0.0:8000"]
