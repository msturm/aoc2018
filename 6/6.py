#!/usr/bin/env python3
import sys

file1 = '6.in'


# Assumption: all coordinates at the edge are infinite
coords = []
with open(file1, 'r') as f:
    for v in f:
        x, y = v.strip().split(',')
        coords.append((int(x), int(y)))
# coords = [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]
max_x = max(coords)[0]
max_y = max(coords, key=lambda a : a[1])[1]

def is_within_range(coords, x, y, range=10000):
    dist_sum = 0
    for a, b in coords:
        p = abs(a-x)
        q = abs(b-y)
        dist_sum += p+q
    # print(dist_sum)
    return dist_sum < range


def find_closest(coords, x, y):
    man_dist = {}
    for u, v in coords:
        man_dist[(u, v)] = max_x+max_y

    for a, b in coords:
        p = abs(a-x)
        q = abs(b-y)
        if man_dist[(a, b)] > p + q:
            man_dist[(a, b)] = p+q
        # print("({0},{1}) -> {2}, {3}".format(a, b, p, q))
    # print(man_dist)
    closest = min(man_dist, key=man_dist.get)
    if list(man_dist.values()).count(man_dist[closest]) > 1:
        closest = '.'
    # print("closest {0}".format(closest))
    return closest


grid = {}
grid2 = {}
for xcoord in range(0, max_x +1):
    for ycoord in range(0, max_y+1):
        grid[(xcoord, ycoord)] = find_closest(coords, xcoord, ycoord)
        grid2[(xcoord, ycoord)] = is_within_range(coords, xcoord, ycoord)

infinite_areas = set()
area_size = {}
for x, y in grid:

    if x == 0 or y == 0 or x == max_x or y == max_y:
        infinite_areas.add(grid[(x, y)])

    if grid[(x, y)] not in infinite_areas:
        if grid[(x, y)] not in area_size:
            area_size[grid[(x, y)]] = 0
        area_size[grid[(x, y)]] += 1



# print(grid)
# print(area_size)
# print(infinite_areas)
print("grid max {0}, {1}".format(max_x, max_y))
max_area = max(area_size, key=area_size.get)
print("largest area: {0}, size {1}".format(max_area, area_size[max_area]))

# print(grid2)
safe_area = list(grid2.values()).count(True)
print("largest safe area: {0}".format(safe_area))
