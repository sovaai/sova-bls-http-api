FROM python:3.7 as build

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
RUN set -eux; \
        apt-get update && apt-get install -y \
        cmake \
        g++ \
        pybind11-dev \
        python3-dev \
        netcat \
        --no-install-recommends && \
    apt-get remove -y --purge software-properties-common && \
    apt-get -y autoremove && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /code
COPY client-lib-py /code/
RUN set -eux; ./rebuild.sh
RUN set -eux; python3 setup.py install

FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive

WORKDIR /code

COPY requirements.txt /code/
COPY  --from=build /code/ /code/client-lib-py/

RUN set -eux; python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN set -eux; cd client-lib-py; python3 setup.py install
COPY api /code/api
COPY external_modules /code/external_modules
COPY kernel /code/kernel
COPY tests /code/tests
COPY *.py /code/
