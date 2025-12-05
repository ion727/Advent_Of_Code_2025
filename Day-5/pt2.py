"""
author: ion727

Advent Of Code: Day 5 (part 2)
"""

with open("data.txt","r") as fp:
    data = fp.read().splitlines()
    i = data.index("")

    instructions = data[:i]
    unique_IDs = set()
    ordered_instructions = []
    for instr in instructions:
        left, right = instr.split("-")
        left, right = ["L",int(left)], ["R",int(right)]
        ordered_instructions.extend((left,right))
    ordered_instructions.sort(key=lambda x:(x[1], 0 if x[0] == "L" else 1)) # con 1: range value; con 2: prioritise L over R to avoid double count
    
    total = 0
    opened = 0
    left, right = 0,0
    for dir, instr in ordered_instructions:
        if dir == "L":
            if opened == 0:
                left = instr
            opened += 1
        else:
            opened -= 1
            if opened == 0:
                right = instr
                total += right - left + 1
print(total)
# Solution: 352556672963116