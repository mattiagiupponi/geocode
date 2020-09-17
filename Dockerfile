FROM python:3.8
COPY . /app
WORKDIR /app
RUN ls -l
RUN pip install -r requirements.txt
WORKDIR /app/geo
CMD python manage.py runserver

