import sys

import requests

sys.path.append('../../..')
from logless import log


@logless.log()
def lambda_handler(event, context):
    session = requests.Session()

    url = event.get('url')

    access_token = {
        'Authorization': 'Bearer {access_token}'
    }

    session.headers.update(access_token)

    r1 = session.get(url)
    r2 = session.get(url)

    return r1, r2
