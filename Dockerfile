FROM python:3.5.4-slim as builder
RUN apt-get update \
    && apt-get -y install curl autoconf automake libtool pkg-config g++ git make \
    && git clone https://github.com/openvenues/libpostal \
    && cd libpostal \
    && ./bootstrap.sh \
    && ./configure  --datadir=/opt/libpostal_data \
    && make \
    && make install DESTDIR=/tmp/libpostal

# Using lightweight alpine image with python3/scipy
FROM python:3.5.4-slim

# we get the previously build libpostal
COPY --from=builder /tmp/libpostal /
COPY --from=builder /opt/libpostal_data /opt/libpostal_data

# Installing packages
RUN apt-get update \
    && apt-get -y install curl autoconf automake libtool pkg-config g++ git make \
    && git clone https://github.com/facebookresearch/fastText.git /opt/fasttext \
    && cd /opt/fasttext \
    && make \
    && pip install pipenv gunicorn==19.7.1 meinheld==0.6.1

ADD app.py Pipfile* /app/

WORKDIR /app

RUN pipenv install --system --deploy

# the sources are copied as late as possible since they are likely to change often
ADD api /app/api

EXPOSE 5000

# Note the number of worker will have a direct impact on the memory consumption, count roughly 2.5G by worker
ENV NB_WORKER 1

ENTRYPOINT gunicorn app:app --workers=${NB_WORKER} --bind=0.0.0.0:5000 --pid=pid --worker-class=meinheld.gmeinheld.MeinheldWorker
