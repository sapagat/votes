build:
	docker-compose build

jupyter: build
	docker-compose up

shell: build
	docker-compose run --rm app pipenv run python
