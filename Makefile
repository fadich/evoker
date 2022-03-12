all: down install build-services up-d logs

install: clean-up
	python setup.py install

clean-up:
	rm -rf build/ dist/ evoker.egg-info

build-services:
	docker-compose build

up:
	docker-compose up --scale worker=10

up-d:
	docker-compose up -d --scale worker=10

down:
	docker-compose down

logs:
	docker-compose logs -f

broker:
	docker-compose up -d rabbitmq

monitor:
	docker-compose up -d flower

worker:
	docker-compose up -d worker
