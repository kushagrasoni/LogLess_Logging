import sys

import requests

sys.path.append('../../..')

import logless


@logless.log(mode="DEV")
def handler(event, context):
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.post(api_url, json=event)
    return response.json()
