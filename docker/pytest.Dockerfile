from python:3.6-slim

run apt update && apt install -y iputils-ping curl

run python -m pip install --upgrade pip

add ./docker/pytest.requirements.txt /tmp

run pip install --no-cache-dir -r /tmp/pytest.requirements.txt

add ./test /test

add ./docker/run_test.sh /tmp/run_test.sh

workdir /test

cmd /tmp/run_test.sh
