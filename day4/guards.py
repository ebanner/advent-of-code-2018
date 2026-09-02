import pandas as pd


with open('guards.txt') as f:
    lines = [line.strip() for line in f.readlines()]

GUARD = None

rows = []

for line in lines:
    ts, *rest = line.split()
    
    if rest[0] == 'Guard':
        _, guard, *_ = rest
        GUARD = guard
    else:
        row = [ts] + [GUARD] + rest
        rows.append(row)

lines = [' '.join(row) for row in rows]

rows = []

for line in lines:
    ts, guard, *rest = line.split()
    ts_ = ts.split(':')[1]
    guard_ = guard.lstrip('#')
    action_  = 'sleep' if ' '.join(rest) == 'falls asleep' else 'wake'
    
    row = [ts_, guard_, action_]
    rows.append(row)

lines = [' '.join(row) for row in rows]

rows = []
for line in lines:
    row = line.split()
    rows.append(row)

df = pd.DataFrame(rows, columns=['ts', 'guard', 'action'])

codes, _ = pd.factorize(df.guard)
df.guard = codes

df = df[['guard', 'ts', 'action']]

df.to_csv('guards.csv', index=False, header=False)

