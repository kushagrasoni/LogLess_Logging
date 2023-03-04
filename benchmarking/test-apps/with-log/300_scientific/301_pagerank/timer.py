import os
import sys
import timeit
import numpy as np
import json
from lambda_local.main import call
from lambda_local.context import Context
import function

num_tests = int(sys.argv[1])
uid = sys.argv[2]
app_nane = os.getcwd().split('/')[-1]

if __name__ == '__main__':

    with open('event.json') as f:
        event = json.load(f)

    durations = []

    for i in range(num_tests):
        print(f"Iter {i}")
        context = Context(i)
        start_time = timeit.default_timer()
        call(function.handler, event, context)
        end_time = timeit.default_timer()
        t = (end_time - start_time)
        durations.append(t)

    d = np.array(durations)
    result = {
        "mean": np.mean(d),
        "min": np.min(d),
        "q25": np.quantile(d, .25),
        "median": np.quantile(d, .50),
        "q75": np.quantile(d, .75),
        "max": np.max(d),
        "std": np.std(d),
        "log_status": "with_log",
        "num_tests": num_tests,
        "app_name": app_nane
    }

    result_json = json.dumps(result)
    with open(f'run_result_{app_nane}_{num_tests}_{uid}.json', 'w') as file:
        file.write(result_json)

    # for i, k in enumerate(result):
    #     duration = "{0:.2f} ms".format(result[k] * 1000)
    #     print(f'{k} time is {duration}')
