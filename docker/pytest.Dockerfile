from python:3.6-slim

run apt update && apt install -y iputils-ping curl

run python -m pip install --upgrade pip

add ./docker/pytest.requirements.txt /tmp

run pip install --no-cache-dir -r /tmp/pytest.requirements.txt

add ./test /test

workdir /test

cmd pytest test.py
