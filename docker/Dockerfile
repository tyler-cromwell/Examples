# Python 3.7 on top of Ubuntu 18.04
FROM ubuntu:18.04

RUN apt update
RUN apt upgrade -y
RUN apt install -y python3.7 python3-pip
RUN rm -f /usr/bin/python3
RUN ln -s /usr/bin/python3.7 /usr/bin/python3
