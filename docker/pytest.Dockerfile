from python:3.6-slim

run python -m pip install --upgrade pip

add ./docker/pytest.requirements.txt /tmp

run pip install --no-cache-dir -r /tmp/pytest.requirements.txt

add ./bot/test /test

workdir /test

cmd pytest test.py
