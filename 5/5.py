#!/usr/bin/env python3
import re

file1 = '5.in'



with open(file1, 'r') as f:
    for v in f:
        raw_polymer = v.strip()
# raw_polymer = "dabAcCaCBACcCaDA"
chars = [chr(i) for i in range(97, 97+26)]
regex = ""
for x in chars:
    # regex += "[" + str(x) + str(x).upper() + "]|"
    regex += str(x) + str(x).upper() + "|" + str(x).upper() + str(x) + "|"
# print(regex[:-1])



minlen = len(raw_polymer)
bad_element = ''

reaction_regex = re.compile(regex[:-1])
for c in chars:
    polymer = re.sub(c, "", raw_polymer, flags=re.IGNORECASE)
    # print(polymer)
    oldlen = len(polymer)
    newlen = 0
    processing_finished = False

    while not processing_finished:
        # print(polymer)
        polymer = reaction_regex.sub("", polymer)
        newlen = len(polymer)
        if oldlen == newlen:
            print("element {0} lenght {1}".format(str(c), str(newlen)))
            if minlen > newlen:
                minlen = newlen
                bad_element = c
            processing_finished = True
        oldlen = newlen

print(minlen)
print(bad_element)
# print(polymer)
