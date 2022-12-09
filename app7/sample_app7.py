import sys

import requests

sys.path.append('..')
import logless


@logless.log(mode='DEV', file_type='pdf')
def lambda_handler(event, context):
    session = requests.Session()

    url = event.get('url')

    access_token = {
        'Authorization': 'Bearer {access_token}'
    }

    session.header.update(access_token)

    r1 = session.get(url)
    r2 = session.get(url)

    return r1, r2
