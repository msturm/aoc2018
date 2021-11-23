#!/usr/bin/env python3
file1 = '3.in'
# file1 = 'test.in'

grid = {}
overlapping = set()
nonoverlapping = set()

with open(file1, 'r') as f:
    for v in f:
        id = v.split('@')[0].strip()[1:]
        dim = v.split('@')[1].split(':')
        x, y = [int(v) for v in dim[0].strip().split(',')]
        w, h = [int(v) for v in dim[1].strip().split('x')]
        print("id {0}, left: {1}, top: {2}, width: {3}, heigth: {4}".format(id, x, y, w, h))
        nonoverlapping.add(id)
        for a in range(x, x + w):
            for b in range(y, y + h):
                coord = str(a) + ',' + str(b)
                if coord not in grid:
                    grid[coord] = id
                else:
                    if grid[coord] in nonoverlapping:
                        nonoverlapping.remove(grid[coord])
                    nonoverlapping.discard(id)
                    overlapping.add(coord)
    print(grid)
    print(overlapping)
    print("overlapping: {0}".format(len(overlapping)))
    print(nonoverlapping)

