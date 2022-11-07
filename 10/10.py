#!/usr/bin/env python3
import os, time, sys
file1 = '10/10.in'

coords = []
vels = []
time_elapsed = 0

def printgrid():
    os.system('clear')
    global minx, maxx, miny, maxy, coords
    stars = {}
    for (x, y) in coords:
        stars[(x,y)] = '*'
    
    for y in range(miny, maxy+1):
        line = []
        for x in range(minx, maxx+1):
            if (x, y) in stars:
                line.append('*')
            else:
                line.append('.')
        print(''.join(line))

def updategrid():
    global coords, vels, minx, maxx, miny, maxy, time_elapsed
    factor = 1 if maxx - minx < 3000 else 100
    time_elapsed = time_elapsed+factor
    for i in range(0, len(vels)):
        coords[i] = (coords[i][0]+(vels[i][0]*factor), coords[i][1]+(vels[i][1]*factor))
    minx, maxx, miny, maxy = 1e5, 0, 1e5, 0
    for (sx, sy) in coords:
        if maxx < sx:
            maxx = sx
        if maxy < sy:
            maxy = sy
        if minx > sx:
            minx = sx
        if miny > sy:
            miny = sy
    

maxx, minx, maxy, miny = 0, 0, 0, 0
with open(file1, 'r') as f:
    for v in f:
        pos, vel = v.strip().split('velocity=')
        sx, sy = [int(x) for x in pos[10:-2].split(',')]
    
        if maxx < sx:
            maxx = sx
        if maxy < sy:
            maxy = sy
        if minx > sx:
            minx = sx
        if miny > sy:
            miny = sy
    
        coords.append((sx, sy))
        vx, vy = [int(x) for x in vel[1:-1].split(',')]
        vels.append((vx, vy))

print(coords, minx, maxx, miny, maxy)
# sys.exit()
smallest = 0
for i in range(0, 150000):
    
    updategrid()
    
    
    if (maxx - minx) < 200 or (maxy - miny) < 200:
        newsize = (maxx - minx) * (maxy-miny)
        if newsize > smallest:
            print(i, minx, maxx, miny, maxy, maxx - minx, maxy-miny)
            print("time elapsed:", time_elapsed - 1)
            sys.exit()
        else:
            os.system('clear')
            smallest = newsize
        printgrid()
        time.sleep(0.2)
    else:
        os.system('clear')
        smallest = (maxx - minx) * (maxy-miny)
        print(i, coords[0])
        print(i, maxx - minx, maxy-miny)
        # print(coords)
        # sys.exit()
        



# printgrid()





