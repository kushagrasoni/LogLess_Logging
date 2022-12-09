import sys

import requests

sys.path.append('..')
# from logless import log


# @log
def lambda_function(event, context):
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.post(api_url, json=event)
    return response.json()
