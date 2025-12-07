"""
author: ion727

Advent Of Code: Day 7 (part 2)
"""

with open("data.txt","r") as fp:
    datalines = fp.read().splitlines()
    start = datalines[0].index("S")
    manifolds = {start:1}
    total = 1
    for i, line in enumerate(datalines): 
        for manifold in list(manifolds.keys()):
            print(manifold)
            if datalines[i][manifold] == "^":
                mani = manifolds.pop(manifold)
                left_key = manifold-1
                if left_key in manifolds:
                    manifolds[left_key] += mani
                else:
                    manifolds[left_key] = mani
                right_key = manifold+1
                if right_key in manifolds:
                    manifolds[right_key] += mani
                else:
                    manifolds[right_key] = mani
total = sum(manifolds.values())
print(total)
# Solution: 17921968177009