from python:3.6-slim

run apt update && apt install -y make curl

run python -m pip install --upgrade pip

run pip install requests rocketchat-py-sdk elasticsearch

add ./analytics /analytics
workdir /analytics

cmd python replay.py
