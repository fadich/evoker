# Invoker

## Installation

### Pre-requirements

#### Python

Install [Python 3.x](https://www.python.org/downloads/).

#### Docker

Install [Docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
and [Docker Compose](https://docs.docker.com/compose/install/).

#### Make

Install `automake`:
```shell
sudo apt-get update
sudo apt-get install -y automake
```

### Build from source

Download the [repository](https://github.com/fadich/evoker)
  or clone it using [Git](https://git-scm.com/downloads):
```shell
git clone git@github.com:fadich/evoker.git
```

Optionally, create [virtual environment](https://realpython.com/python-virtual-environments-a-primer/) for Python:
```shell
virtualenv -p python3 venv
source venv/bin/activate
```

Install the package and build services:
```shell
make install
make build-services
```

#### Run via Docker Compose

You can run all the services with docker-compose by executing:
```shell
make up
```

The monitor service (Flower) in deployed on
  [0.0.0.0:5555](http://0.0.0.0:5555).

For run the installation and docker-compose services you may
  only call `make` command.

To stop all the services run:
```shell
make down
```

#### Run the Client (Evoke!)

Run the `evoker-cli` script. Usage:
```shell
usage: evoker-cli [-h] [-d] [-c CONCURRENCY] [-i INTERVAL] N [N ...]

positional arguments:
  N                     urls to be called

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           set debug log level
  -c CONCURRENCY, --concurrency CONCURRENCY
                        number of concurrent requests
  -i INTERVAL, --interval INTERVAL
                        repeat every X seconds


```

For example, make 2 requests to the monitor (flower) service
every 10 seconds:
```shell
evoker-cli -c 2 -i 10 http://flower:5555/broker
```

#### Other Make commands

View the services logs, run:
```shell
make logs
```

Run broker:
```shell
make broker
```

Run worker:
```shell
make worker
```

Remove all build files:
```shell
make clean-up
```
