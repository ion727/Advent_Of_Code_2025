"""
author: ion727

Advent Of Code: Day 6 (part 2)
"""

import numpy as np
from itertools import groupby

def prod(iterable):
    product = 1
    for i in iterable:
         product *= i
    return product

total = 0
with open("data.txt", "r") as fp:
    raw = fp.read().splitlines()
    *datalines, operators = raw
    datalines = np.array([list(line) for line in datalines]).swapaxes(0,1)
    datalines = [''.join(row) for row in datalines]
    datalines = [list(group) for key, group in groupby(datalines, key=lambda x: x.strip() == "") if not key]
    datalines = [[int(item.strip()) for item in row] for row in datalines]
    operators = operators.split()
    sums = [sum(line) for line in datalines]
    prods = [prod(line) for line in datalines]
    for index, op in enumerate(operators):
            total += sums[index] if op == "+" else prods[index]
print(total)
# Solution: 9434900032651