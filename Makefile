first-run:
	cd docker && ./build-base.sh
	docker-compose up -d rocketchat
	make train
	docker-compose run --rm bot make config-rocket
	docker-compose up bot

train:
	docker build . -f docker/coach.Dockerfile -t botcoach:latest
	docker-compose build bot

console:
	docker-compose run bot make run-console
