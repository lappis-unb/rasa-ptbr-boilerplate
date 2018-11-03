from python:3.6-slim

run apt update && apt install -y make curl

run python -m pip install --upgrade pip

add ./actions.requirements.txt /tmp
run pip install --no-cache-dir -r /tmp/actions.requirements.txt

add ./rouana/actions /bot/actions
add ./rouana/Makefile /bot

workdir /bot

expose 5055
healthcheck --interval=300s --timeout=60s --retries=5 \
  cmd curl -f http://0.0.0.0:5055/health || exit 1

cmd make run-actions
