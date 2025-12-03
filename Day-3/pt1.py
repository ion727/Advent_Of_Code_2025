"""
author: ion727

Advent Of Code: Day 3 (part 1)
"""

total = 0
with open("example.txt", "r") as fp:
    datalines = fp.read().split("\n")
    for line in datalines:
        first, second = 0,0
        end = len(line)-1
        for index,char in enumerate(line):
            num = int(char)
            if num > first and index != end:
                first = num
                second = 0
            elif num > second:
                second = num
            print(list(map(int,list(str(a)))))
        total += (a:=first*10 + second)
print(total)
# Solution: 17408