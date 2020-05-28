# Base image to build on
FROM dockbase:1.0

# Create docker user
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo
USER docker
WORKDIR /home/docker
