import sys
from time import sleep

sys.path.append('../../../..')

import logless


@logless.log(mode="DEV", file_type="log", file_name="sleep")
def handler(event, context):
    # start timing
    sleep_time = event.get('sleep')
    sleep(sleep_time)
    return {'result': sleep_time}
