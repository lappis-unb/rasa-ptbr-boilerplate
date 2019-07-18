import requests 
import json

def get_request(payload, url):
    header = {"content-type": "application/json"}
    return requests.get(url, data=payload, headers=header).json()

def post_request(payload, url):
    header = {"content-type": "application/json"}
    return requests.post(url, data=payload, headers=header).json()
