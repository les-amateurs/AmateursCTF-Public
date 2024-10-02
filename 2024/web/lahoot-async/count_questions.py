import sys

import json

count = 0
with open(sys.argv[1], "r") as f:
    for line in f:
        try:
            count += len(json.loads(line))
        except:
            pass
    
print(count, " questions are in this set.")