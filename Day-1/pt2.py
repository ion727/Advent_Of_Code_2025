"""
author: ion727

Advent Of Code: Day 1 (part 2)
"""

password = 0
with open("data.txt", "r") as fp:
    datalines = fp.readlines()
    ptr = 50
    for data in datalines:
        sign, *num = data
        num = int("".join(num).strip("\n"))
        coeff = -1 if sign == "L" else 1
        for _ in range(num):
            ptr += coeff
            ptr %= 100
            if ptr == 0:
                password += 1
print(password)
# Solution: 5847