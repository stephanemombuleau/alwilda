FROM alpine:3.6 as builder
RUN apk update \
    && apk add findutils autoconf automake libtool curl git g++ make\
    && git clone https://github.com/openvenues/libpostal \
    && cd libpostal \
    && ./bootstrap.sh \
    && ./configure  --datadir=/opt/libpostal_data \
    && make \
    && make install DESTDIR=/tmp/libpostal

# Using lightweight alpine image with python3/scipy
FROM antoinede/alpine-3.6-python-3.6-scipy

# we get the previously build libpostal
COPY --from=builder /tmp/libpostal /
COPY --from=builder /opt/libpostal_data /opt/libpostal_data

# Installing packages
RUN apk update \
    && apk add g++ musl-dev make python3-dev git\
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

ENV NB_WORKER 1

ENTRYPOINT gunicorn app:app --workers=${NB_WORKER} --bind=0.0.0.0:5000 --pid=pid --worker-class=meinheld.gmeinheld.MeinheldWorker
