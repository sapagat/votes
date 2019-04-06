build:
	docker-compose build

jupyter: build
	docker-compose up
