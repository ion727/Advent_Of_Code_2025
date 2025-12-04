"""
author: ion727

Advent Of Code: Day 4 (part 2)
"""
def generate_positions(grid, coords):
    tx, ty = coords
    height, width = len(grid), len(grid[0])
    positions = [(tx+x-1,ty+y-1) for x in range(3) for y in range(3) if 0 <= tx+x-1 < width and 0 <= ty+y-1 < height]
    positions.remove(coords)
    return positions

total = 0
with open("data.txt", "r") as fp:
    datalines = [list(string) for string in fp.read().splitlines()]
    maxlen = len(datalines[-1])
    datalines = [line[:maxlen] for line in datalines]
    changed = True
    while changed:
        changed = False
        for y,row in enumerate(datalines):
            for x,column in enumerate(row):
                counter = 0
                if datalines[y][x] != "." and [datalines[gy][gx] for gx,gy in generate_positions(datalines, (x,y))].count("@") < 4:
                    datalines[y][x] = "."
                    total += 1
                    changed = True
# Solution: 8409