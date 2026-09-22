import pandas as pd
from datetime import datetime


with open('input') as f:
    lines = [line.strip() for line in f.readlines()]

dts = []
rests = []
for line in lines:
    tokens = line.split()
    ts, rest = ' '.join(tokens[:2]), ' '.join(tokens[2:])

    dt = datetime.strptime(ts, "[%Y-%m-%d %H:%M]")
    
    dts.append(dt)
    rests.append(rest)

df = pd.DataFrame({'dt': dts, 'rest': rests}).sort_values(by='dt')

print(df)
print()

rows = []
for dt, rest in df.values.tolist():
    row = [dt.strftime("%H:%M"), rest]
    rows.append(row)

lines = []
for row in rows:
    line = ' '.join(row)
    lines.append(line)

for line in lines:
    print(line)
print()

GUARD = None

rows = []
for line in lines:
    tokens = line.split()
    ts, *rest = tokens
    
    if rest[0] == 'Guard':
        _, guard, *_ = rest
        GUARD = guard
    else:
        row = [ts] + [GUARD] + rest
        rows.append(row)

lines = [' '.join(row) for row in rows]

for line in lines:
    print(line)
print()

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
df['index'] = codes + 1

df = df[['index', 'ts', 'guard', 'action']]

df.to_csv('guards.csv', index=False, header=False)
