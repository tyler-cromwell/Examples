# Docker
This is an example of how to build a simple [Docker][docker] container.
Specifically, the Dockerfile defines an Ubuntu 18.04 image containing Python 3.7.

Commands:
  - Build: `docker build -t python:3.7 ./`
  - Run/Test: `docker run -it --rm python:3.7 bash` (opens a bash terminal into the container)

[docker]: https://www.docker.com/
