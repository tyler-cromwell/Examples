# Docker
This is an example of a simple [Docker][docker] image that installs additional packages onto the container's operating system.
Specifically, the Dockerfile defines the instructions to build a container running [Ubuntu][ubuntu] 19.04 that installs [Python 3.8][python] and [Django][django] 3.0.2.

Commands:
  - Build: `docker build -t django:3.0.2 ./`
  - Run/Test: `docker run -it --rm django:3.0.2 bash` (opens a bash terminal into the container)

[docker]: https://en.wikipedia.org/wiki/Docker_%28software%29
[django]: https://en.wikipedia.org/wiki/Django_(web_framework)
[python]: https://en.wikipedia.org/wiki/Python_%28programming_language%29
[ubuntu]: https://en.wikipedia.org/wiki/Ubuntu
