import timeit
import numpy as np
import pandas as pd
import json
from lambda_local.main import call
from lambda_local.context import Context
import sample_app1

with open('event.json') as f:
    event = json.load(f)

context = Context(1)

num_tests = 10

durations = []

#call once to initialise enviornment
call(sample_app1.lambda_handler, event, context)

for i in range(num_tests):
    context = Context(i)
    start_time = timeit.default_timer()
    call(sample_app1.lambda_handler, event, context)
    end_time = timeit.default_timer()
    t = (end_time - start_time)
    durations.append(t)

d = np.array(durations)
res = {
    'mean' : np.mean(d),
    'min' : np.min(d),
    'q25' : np.quantile(d,.25),
    'median' : np.quantile(d,.50),
    'q75' : np.quantile(d,.75),
    'max' : np.max(d),
    'std' : np.std(d)
}


for i, k in enumerate(res):
    duration = "{0:.2f} ms".format(res[k] * 1000)
    print(f'{k} time is {duration}')