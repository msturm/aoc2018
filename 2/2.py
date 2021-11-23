#!/usr/bin/env python3
import sys
file1 = '2.in'

twice = 0
thrice = 0
ids = []

def matchids(s1, s2): 
    diffcount = 0
    diffindex = 0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            diffcount += 1
            diffindex = i 
    
    if diffcount == 1:
        return diffindex
    else:
        return 0
with open(file1, 'r') as f:
    for v in f:
        ids.append(v)
        L = {}
        for l in v:
            L[l] = L.get(l, 0) + 1
        if 2 in L.values():
            twice += 1
        if 3 in L.values():
            thrice += 1

print(str(twice) + " " + str(thrice))
print(str(twice * thrice))

for a in range(0, len(ids)):
    for b in range(0, len(ids)):
        if a != b: 
            matchid = matchids(ids[a], ids[b]) 
            if matchid > 0 :
                print("match " + str(matchid))
                print(ids[a]) 
                print(ids[b])
                print(str(a) + " " + str(b) + " ") 
                print(ids[a][:matchid] + ids[a][matchid+1:])
                sys.exit(0)
            


