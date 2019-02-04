# Base image to build on
FROM ubuntu:18.04

# Image metadata
LABEL maintainer="tjc6185@gmail.com"
LABEL version="1.0.0"
LABEL description="Django 2.1.5 and Python 3.7 installed on Ubuntu 18.04"

# Commands executed inside container during build
RUN apt update && apt install -y python3.7 python3-pip
RUN rm -f /usr/bin/python3
RUN ln -s /usr/bin/python3.7 /usr/bin/python3
RUN pip3 install django==2.1.5
