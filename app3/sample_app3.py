import sys

import requests

sys.path.append('..')
import logless


@logless.log()
def lambda_function(event, context):
    api_url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.post(api_url, json=event)
    return response.json()
