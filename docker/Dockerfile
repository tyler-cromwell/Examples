# Base image to build on
FROM ubuntu:19.04

# Image metadata
LABEL maintainer="tjc6185@gmail.com"
LABEL version="1.0.0"
LABEL description="Django 3.0.2 and Python 3.8 installed on Ubuntu 19.04"

# Commands executed inside container during build
RUN apt update && apt install --no-install-recommends -y python3.8 python3-pip
RUN rm -f /usr/bin/python3
RUN ln -s /usr/bin/python3.8 /usr/bin/python3
RUN pip3 install django==3.0.2
