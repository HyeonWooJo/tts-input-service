FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN apt-get -y update
RUN apt-get -y install vim
RUN mkdir /backend
ADD . /backend

WORKDIR /backend
ADD requirements.txt /backend

RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt