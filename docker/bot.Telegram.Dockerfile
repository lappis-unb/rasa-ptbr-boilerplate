FROM python:3.6-slim

RUN apt-get update && apt-get install -y git gcc make curl

ADD ./bot/requirements.txt /tmp
ADD ./bot /bot
ADD ./scripts /scripts

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    python -c "import nltk; nltk.download('stopwords');"

WORKDIR /bot

RUN apt-get -yq remove --purge --auto-remove -y ${BUILD_PACKAGES}; \
    apt-get -yq clean; \
    apt-get -yq autoclean; \
    apt-get -yq autoremove; \
    rm -rf /tmp/* /var/tmp/*; \
    rm -rf /var/lib/apt/lists/*; \
    rm -rf /var/cache/apt/archives/*.deb \
        /var/cache/apt/archives/partial/*.deb \
        /var/cache/apt/*.bin; \
    find /usr/lib/python3 -name __pycache__ | xargs rm -rf; \
    find /bot -name __pycache__ | xargs rm -rf; \
    rm -rf /root/.[acpw]*;

CMD make train && python run-telegram.py
