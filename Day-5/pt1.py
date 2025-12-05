"""
author: ion727

Advent Of Code: Day 5 (part 1)
"""
with open("data.txt","r") as fp:
    data = fp.read().splitlines()
    i = data.index("")

    total = 0
    instructions, ingredients = data[:i], data[i+1:]
    for ingr in ingredients:
        ingr = int(ingr)
        for instr in instructions:
            left, right = instr.split("-")
            left, right = int(left), int(right)
            if left <= ingr <= right:
                total += 1
                break
print(total)
# Solution: 865