import logging
import os
import argparse

from elasticsearch import Elasticsearch

parser = argparse.ArgumentParser(description='configures elastic')
parser.add_argument('--task', '-t', default='setup', choices=['setup', 'delete'],)
args = parser.parse_args()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

es = Elasticsearch([os.getenv('ELASTICSEARCH_URL', 'elasticsearch:9200')])

settings = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0
    },
    "mappings": {
        "message": {
            "properties": {
                "environment":       { "type": "text" },
                "version":           { "type": "text" },
                "user_id":           { "type": "text" },
                "is_bot":            { "type": "boolean" },
                "text":              { "type": "text" },
                "timestamp":         { "type": "date" },
                "intent_name":       { "type": "text" },
                "intent_confidence": { "type": "text" },
                "entities" :         { "type": "text" },
                "utter_name":        { "type": "text" },
                "is_fallback":       { "type": "boolean" },
            }
        }
    }
}

index_name = 'messages'

if __name__ == '__main__':
    if args.task == 'setup':
        try:
            if not es.indices.exists(index_name):
                logger.debug(es.indices.create(index=index_name, ignore=400,
                                               body=settings))
                logger.info('Created Index')
            else:
                logger.info('Index {} already exists'.format(index_name))
        except Exception as ex:
            logger.error(str(ex))

    elif args.task == 'delete':
        logger.debug(es.indices.delete(index=index_name, ignore=[400, 404]))
        logger.info('Index deleted')
