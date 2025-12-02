"""
author: @ion727

Advent Of Code: Day 2 (part 1)
"""

def is_valid(num):
    # split string in half and compare halves
    num = str(num)
    m = len(num)//2 
    left, right = num[:m], num[m:]
    return left == right

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
# Solution: 64215794229