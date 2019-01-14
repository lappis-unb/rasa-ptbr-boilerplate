echo "Checking if the training has already been done."

if [ ! -d "models/dialogue/" ]; then
	echo "bot/models/dialogue folder does not exist, making training."
	make train
fi

echo "Starting bot API for tests"
make run-test
