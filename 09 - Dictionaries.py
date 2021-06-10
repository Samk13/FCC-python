
import json
counts = dict()

with open('comments.json') as json_file:
    data = json.load(json_file)
    for d in data:
        for p, n in d.items():
            counts[p] = counts.get(p, 0) + 1
print('COUNTS: ', counts)
