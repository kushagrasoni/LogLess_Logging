import sys

import requests

sys.path.append('../../../..')

import logless


@logless.log(file_type='txt', file_name='auth')
def handler(event, context):
    session = requests.Session()

    url = event.get('url')

    access_token = {
        'Authorization': 'Bearer {access_token}'
    }

    session.headers.update(access_token)

    r1 = session.get(url)

    return r1
