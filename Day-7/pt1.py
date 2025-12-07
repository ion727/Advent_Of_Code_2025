"""
author: ion727

Advent Of Code: Day 7 (part 1)
"""
with open("data.txt","r") as fp:
    datalines = fp.read().splitlines()
    start = datalines[0].index("S")
    manifolds = [start]
    new = []
    total = 0
    for i, line in enumerate(datalines): 
        #print([datalines[i][manifold] for manifold in manifolds])
        for manifold in manifolds[:]:
            if datalines[i][manifold] == "^":
                total += 1
                if manifold-1 not in new:
                    new.append(manifold-1)
                if manifold+1 not in new:
                    new.append(manifold+1)
                manifolds.remove(manifold)
        for manifold in new:
            if manifold not in manifolds:
                manifolds.append(manifold)
        new.clear()
print(total)
# Soluton: 1592