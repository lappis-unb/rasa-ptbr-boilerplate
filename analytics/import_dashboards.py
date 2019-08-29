import json
import requests
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def getIdDashboards(pathToFile):
    dashboardsIds = {}

    # Path that contains the data of the export.json to search dashboard id's
    # export.json from version 7.3 of kibana
    with open(pathToFile) as file:
        data = json.load(file)

        for savedObjects in data['saved_objects']:
            attributes = savedObjects['attributes']['title']
            dashboardsIds[attributes] = savedObjects['id']

    return dashboardsIds


def importDashboards(pathToFile):
    URL = os.getenv('KIBANA_URL', 'http://localhost:5601')
    fullURL = URL + '/api/kibana/dashboards/import?exclude=index-pattern'

    header = {
        'kbn-xsrf': 'true',
        'Content-Type': 'application/json'
    }

    datas = open(pathToFile, 'rb').read()
    datas = datas.decode("utf-8")

    request = requests.post(url=fullURL, headers=header, data=json.dumps(datas))


if __name__ == "__main__":
    try:
        importDashboards('analytics/dashboards.json')
    except Exception as ex:
        logger.error(str(ex))
