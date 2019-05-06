train: 
	docker build . -f docker/coach.Dockerfile -t coach:latest

first-run:
	cd docker && ./build-base.sh
	make train
	docker-compose up --build bot
