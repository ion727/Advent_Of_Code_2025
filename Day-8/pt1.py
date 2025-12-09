"""
author: ion727

Advent Of Code: Day 8 (part 1)
"""

def deep_search(box, visited):
    total = 1
    for target in box.connections[:]:
        if target not in visited:
            visited.add(target)
            total += deep_search(target, visited)
    return total

class Box:
    def __init__(self, coords):
        x,y,z = coords
        self.x,self.y,self.z = int(x), int(y), int(z)
        self.closests = []
        self.connections = []
    
    @property
    def key(self):
        k = [((self, close[0]), close[1]) for close in self.closests]
        k.sort(key=lambda x:x[1])
        return k
        
with open("data.txt","r") as fp:
    SIZE = 1000
    total = 1
    totals=[]
    datalines = fp.read().splitlines()
    coords = [line.split(",") for line in datalines]
    boxes = [Box(coord) for coord in coords]
    for box in boxes:
        for target in boxes:
            if box is target:
                continue
            dx = abs(box.x - target.x)
            dy = abs(box.y - target.y)
            dz = abs(box.z - target.z)
            distance = (dx**2 + dy**2 + dz**2)**(1/2)
            box.closests.append([target, distance])
        box.closests.sort(key=lambda x:x[1])
    paired_distances = [key for box in boxes for key in box.key]
    #paired_distances.sort(key=lambda x:sum((sum(i.coords) for i in x[0])))
    paired_distances.sort(key=lambda x:x[1])
    paired_distances= paired_distances[::2]
    for i in range(SIZE):
        box, target = paired_distances[i][0]
        box.connections.append(target)
        target.connections.append(box)
    visited = set()
    for box in boxes:
        if box not in visited:
            visited.add(box)
            connections = deep_search(box, visited)
            totals.append(connections)
totals.sort(reverse=True)
one, two, three = totals[:3]
total = one*two*three
print(total)
# Solution: 84968