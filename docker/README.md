# Docker
This is an example of a simple [Docker][docker] image that installs additional packages onto the container's operating system.
Specifically, the Dockerfile defines the instructions to build a container running Ubuntu 18.04 that installs [Python 3.7][python] and [Django][django] 2.1.5.

Commands:
  - Build: `docker build -t django:2.1.5 ./`
  - Run/Test: `docker run -it --rm django:2.1.5 bash` (opens a bash terminal into the container)

[docker]: https://en.wikipedia.org/wiki/Docker_%28software%29
[django]: https://en.wikipedia.org/wiki/Django_(web_framework)
[python]: https://en.wikipedia.org/wiki/Python_%28programming_language%29
