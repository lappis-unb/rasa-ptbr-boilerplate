#!/usr/bin/env python
import pika
import os
import json
import logging
from elastic_connector import ElasticConnector

username = os.getenv('RABBITMQ_DEFAULT_USER')
password = os.getenv('RABBITMQ_DEFAULT_USER')
credentials = pika.PlainCredentials(username, password)

logger = logging.getLogger(__name__)

_elastic_connector = None

elastic_user = os.getenv('ELASTICSEARCH_USER')
if elastic_user is None:
    _elastic_connector = ElasticConnector(
        domain=os.getenv('ELASTICSEARCH_URL', 'elasticsearch:9200')
    )
else:
    _elastic_connector = ElasticConnector(
        domain=os.getenv('ELASTICSEARCH_URL', 'elasticsearch:9200'),
        user=os.getenv('ELASTICSEARCH_USER', 'user'),
        password=os.getenv('ELASTICSEARCH_PASSWORD', 'password'),
        scheme=os.getenv('ELASTICSEARCH_HTTP_SCHEME', 'http'),
        scheme_port=os.getenv('ELASTICSEARCH_PORT', '80')
    )

connection = pika.BlockingConnection(
                pika.ConnectionParameters(
                   host='rabbitmq', credentials=credentials,
                   connection_attempts=20, retry_delay=5
                )
             )

channel = connection.channel()
channel.queue_declare(queue='bot_messages', durable=True)


def callback(ch, method, properties, body):
    logger.warning(" [x] Received %r" % body)

    message = json.loads(body.decode('utf-8'))

    if message['event'] == 'user':
        _elastic_connector.save_user_message(message)
        _elastic_connector.previous_user_message = message

    elif message['event'] == 'action':
        if message['name'] == 'action_listen':
            _elastic_connector.previous_action = None
            return

        _elastic_connector.previous_action = message

    elif message['event'] == 'bot':
        if _elastic_connector.previous_action is None:
            _elastic_connector.previous_user_message = None
            return

        bot_message = message
        action_message = _elastic_connector.previous_action
        previous_user_message = _elastic_connector.previous_user_message

        _elastic_connector.save_bot_message(bot_message,
                                            action_message,
                                            previous_user_message)


if __name__ == '__main__':
    channel.basic_consume(
            queue='bot_messages', on_message_callback=callback, auto_ack=True)

    logger.warning('[*] Waiting for messages.')
    channel.start_consuming()
