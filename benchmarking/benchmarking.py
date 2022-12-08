from pathlib import Path
import os
import sys
import subprocess
wd = os.getcwd()

from tqdm import tqdm
os.chdir(wd)

timers = [x for x in Path('test-apps').rglob('timer.py')]
int_runs = [100, 1000, 2000, 3000, 4000, 5000]

uid = 'uid002'
for n in int_runs:
    s = str(n)
    print(f"Running for {n}")
    for path in tqdm(timers, file=sys.stdout):
        # if 'app2' in path.parent.name:
        os.chdir(wd)
        sys.path.append(path.parent)
        
        # result = subprocess.run(['python', ''], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        os.chdir(path.parent)
        r = subprocess.run(["python", path.name, s, uid],stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, text=True)


os.chdir(wd)

uid = 'uid002'
import json
import pandas as pd
recs = []

for p in Path('test-apps').rglob(f'run_result_*_{uid}.json'):
    with open(p) as f:
        d = json.load(f)
        recs.append(d)

df = pd.DataFrame.from_records(recs)

df['time'] = df['mean'] * df['num_tests']

p_df = df.pivot_table(columns=['app_name','log_status','num_tests'])
p_df.to_csv(f'benchmarking_results.csv',index=True)
df.to_csv(f'benchmarking_{uid}.csv',index=False)