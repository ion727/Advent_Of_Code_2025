"""
author: ion727

Advent Of Code: Day 6 (part 1)
"""
import numpy as np

total = 0
with open("data.txt", "r") as fp:
    *datalines, operators = fp.read().splitlines()
    datalines = np.array([line.split() for line in datalines])
    datalines = [list(map(int, line)) for line in datalines]
    operators = operators.split()
    sums = np.sum(datalines, axis=0)
    prods = np.prod(datalines, axis=0)
    for index, op in enumerate(operators):
            total += sums[index] if op == "+" else prods[index]
print(total)
# Solution: 5667835681547