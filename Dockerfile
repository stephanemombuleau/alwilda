# Using lightweight alpine image
FROM python:3.6-alpine3.6

# Installing packages
RUN apk update && apk add gcc musl-dev

RUN mkdir /app
ADD api /app/api
ADD app.py Pipfile* /app/

RUN pip install pipenv

WORKDIR /app

RUN pipenv install --system --deploy
RUN pip install gunicorn==19.7.1 meinheld==0.6.1


EXPOSE 5000

ENTRYPOINT gunicorn app:app --workers=4 --bind=0.0.0.0:5000 --pid=pid --worker-class=meinheld.gmeinheld.MeinheldWorker
