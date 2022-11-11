#!/usr/bin/env python3
file1 = '11.in'

# with open(file1, 'r') as f:
    # for v in f:

# cache = {}
cache2 = {}
def calc_power(x, y, serial):
    # if (x, y) not in cache:
        rack_id = x+10
        power = rack_id * y
        power += serial
        power = power * rack_id
        power = int((power // 100) % 10)
        return power - 5
    # print("calc_power", x, y, serial)
    # return cache[(x, y)]


def calc_block(x, y, z, serial):
    global cache2
    result = 0
    if x + z > 301 or y + z > 301:
        return 0
    if (x, y, z) in cache2:
        return cache2[(x, y, z)]
    else:
        if z > 1:
            new_value = calc_block(x, y, z-1, serial)
            # print(z, new_value)
            for dy in range(y, y+z):
                new_value += calc_power(x+z-1, dy, serial)
            # print(2, new_value)
            for dx in range(x, x+z):
                new_value += calc_power(dx, y+z-1, serial)
            new_value -= calc_power(x+z-1, y+z-1, serial)
            # print(3, new_value)
                # print(dx, dy, calc_power(dx, dy, serial))
            cache2[(x, y, z)] = new_value
        else:
            cache2[(x, y, z)] = calc_power(x, y, serial)
        return cache2[(x, y, z)]

# print(calc_block(33, 45, 18))
# assert False
assert calc_power(3, 5, 8) == 4
# print(calc_power(3, 5, 8))
assert calc_power(122, 79, 57) == -5
# print(calc_power(122, 79, 57))
assert calc_power(217, 196, 39) == 0
# print(calc_power(217, 196, 39))
assert calc_power(101, 153, 71) == 4
# print(calc_power(101, 153, 71))

serial = 5791
# serial = 42
# print(calc_block(33,45,3,18))
# assert calc_block(33,45,3,18) == 29
# assert calc_block(90, 269, 16, 18) == 113
# assert calc_block(232, 251, 12, 42) == 119
# assert calc_block(89, 269, 16, 5791) == 119
# assert calc_block(89, 269, 17, 42) == 124
# print(calc_block(89, 269, 16, 42))
# print(calc_block(89, 269, 17, 42))
# print(calc_power(105,269, 42))
print('--------------')
# print(calc_block(90, 269, 17, serial))
# for y in range(269, 269+17):
    # print("\t".join([str(cache[(x, y)]) for x in range(89, 89+17)]))

print("\n")
# for y in range(269, 269+17):
    # print("\t".join([str(calc_power(x, y, serial)) for x in range(90, 90+17)]))
# print(cache)

# print(cache2)
# assert False

for x in range(1, 298):
    for y in range(1, 298):
        cache2[(x, y, 1)] = calc_power(x, y, serial)

max_block_power = 0
max_xyz = (0,0,1)
for gz in range(1, 300):
    print(gz, max_xyz, max_block_power)
    for gy in range(1, 298):
        for gx in range(1, 298):
            block_power = calc_block(gx, gy, gz, serial)
            if block_power > max_block_power:
                max_block_power = block_power      
                max_xyz = (gx, gy, gz)

print(max_block_power, max_xyz)
