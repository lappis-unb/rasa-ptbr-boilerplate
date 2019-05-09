train: 
	docker build . -f docker/coach.Dockerfile -t botcoach:latest
	docker-compose build bot

first-run:
	cd docker && ./build-base.sh
	make train
	docker-compose up bot
