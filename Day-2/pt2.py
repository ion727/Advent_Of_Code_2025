"""
author: ion727

Advent Of Code: Day 2 (part 2)
"""

import re
def is_valid(num):
    expr = r'(\d+)\1+'
    return re.fullmatch(expr, str(num))

total = 0
with open("data.txt","r") as fp:
    data = fp.read().split(",")
    data = [range_.split("-") for range_ in data]
    for range_ in data:
        start, end = range_
        for i in range(int(start), int(end)+1):
            if is_valid(i):
                total += i
print(total)
# Solution: 85513235135