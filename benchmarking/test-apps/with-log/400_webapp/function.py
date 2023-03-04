from datetime import datetime
from random import sample
from os import path
import sys

from jinja2 import Template

sys.path.append('../..')

import logless

SCRIPT_DIR = path.abspath(path.join(path.dirname(__file__)))


@logless.log(mode="PROD", file_type='log', file_name='webapp')
def handler(event, context=None):
    name = event.get('username')
    size = event.get('size')
    cur_time = datetime.now()
    random_numbers = sample(range(0, 1000000), size)
    template = Template(open(path.join(SCRIPT_DIR, "templates", "template.html"), 'r').read())
    html = template.render(username=name, cur_time=cur_time, random_numbers=random_numbers)
    f = open('result.html', 'w')
    f.write(html)
    f.close()
    return None
