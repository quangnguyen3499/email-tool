FROM python:3.10

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get upgrade -y

RUN pip install django
RUN pip install gunicorn
RUN pip install django-environ
RUN pip install django-celery-beat
RUN pip install django-celery-results
RUN pip install djangorestframework-simplejwt
RUN pip install psycopg2-binary
RUN pip install whitenoise
RUN pip install django-allauth
RUN pip install django-structlog
RUN pip install drf-spectacular

WORKDIR /app
COPY . /app

EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]