build:
	docker-compose build

jupyter: build
	docker-compose up

python: build
	docker-compose run --rm app pipenv run python

check:
	docker-compose run --rm app /bin/sh check_notebooks.sh
