"""
author: ion727

Advent Of Code: Day 4 (part 1)
"""

# Generates a list of available slots coordinates
def generate_positions(grid, coords):
    tx, ty = coords
    height, width = len(grid), len(grid[0])
    positions = [(tx+x-1,ty+y-1) for x in range(3) for y in range(3) if 0 <= tx+x-1 < width and 0 <= ty+y-1 < height]
    positions.remove(coords)
    return positions

total = 0
with open("data.txt", "r") as fp:
    datalines = fp.read().splitlines()
    for y,row in enumerate(datalines):
        for x,column in enumerate(row.strip("\n")):
            counter = 0
            if datalines[y][x] != "." and [datalines[gy][gx] for gx,gy in generate_positions(datalines, (x,y))].count("@") < 4:
                total += 1
print(total)
# Solution: 1464