import json
import requests
import os
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def getRequestDatas(finalUrl):
    fullUrl = []

    url = os.getenv("KIBANA_URL", "http://kibana:5601")
    url = url + finalUrl

    header = {"kbn-xsrf": "true", "Content-Type": "application/json"}

    fullUrl.append(url)
    fullUrl.append(header)

    return fullUrl


def getIdDashboards(pathToFile):
    dashboardsIds = {}

    # Path that contains the data of the export.json to search dashboard id's
    # export.json from version 7.3 of kibana
    with open(pathToFile) as file:
        data = json.load(file)

        for savedObjects in data["saved_objects"]:
            attributes = savedObjects["attributes"]["title"]
            dashboardsIds[attributes] = savedObjects["id"]

    return dashboardsIds


def importDashboards(pathToFile):
    finalUrl = "/api/kibana/dashboards/import?exclude=index-pattern"
    requestData = getRequestDatas(finalUrl)

    datas = open(pathToFile, "rb").read()
    datas = datas.decode("utf-8")

    requests.post(url=requestData[0], headers=requestData[1], data=json.dumps(datas))

    createIndexPattern()


def createIndexPattern():
    # TODO: Import value of the variable from the environment
    idIndex = "194404f0-e6b4-11e8-bb67-918dc5752875"
    finalUrl = "/api/saved_objects/index-pattern/" + idIndex

    requestData = getRequestDatas(finalUrl)

    datas = {"attributes": {"title": "messages*"}}

    requests.post(url=requestData[0], headers=requestData[1], data=json.dumps(datas))


if __name__ == "__main__":
    try:
        importDashboards("./dashboards.json")
    except Exception as ex:
        logger.error(str(ex))
