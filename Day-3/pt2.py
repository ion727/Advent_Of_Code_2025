"""
author: ion727

Advent Of Code: Day 3 (part 2)
"""
VERBOSE = False

total = 0
with open("data.txt", "r") as fp:
    datalines = fp.read().split("\n")
    for line in datalines:
        n = 12
        vals = [0]*n
        length = len(line)
        if VERBOSE:print(f"check line:{line}")
        for index, char in enumerate(line): # iterate through items in line
            if VERBOSE:print(f"\n\ncheck index {index}: {char}")
            num = int(char)
            for k, best_val in enumerate(vals): # iterate through stored values
                if VERBOSE:print(f"compare element {k}: {best_val} to element {index}: {char}")
                if index - length + n <=  k and num > best_val:
                    if VERBOSE:print("successful comparison, assigning new value and replacing subsequents")
                    vals[k] = num
                    if VERBOSE:print(f"1. state after initial replacement of index {k}: {vals}")
                    # replace every next value with 0
                    for i in range(k+1, n):
                        if VERBOSE:print(f"replacing element {i}")
                        vals[i] = 0
                    if VERBOSE:print(f"replacemenent completed: {vals}\n")
                    break
        total += int(''.join(list(map(str, vals))))
print(total)
# Solution: 172740584266849