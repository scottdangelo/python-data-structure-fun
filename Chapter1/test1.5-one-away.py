#! /usr/bin/env python

in_string1 = "bale"
in_string2 = "palex"

l1 = list(in_string1)
l2 = list(in_string2)
l1_orig = list(in_string1)
l2_orig = list(in_string2)

x = 0
ret = True
if abs(len(l1) - len(l2)) >1:
    ret = False
off_count = 1

while x < len(l1) and ret:
    if l1[x] not in l2:
        if off_count == 0:
            ret = False
            break
#        l1_orig.remove(l1[x])
        off_count -= 1
        x = x +1
    else:
#        l1_orig.remove(l1[x])
#        l2_orig.remove(l1[x])
        x = x +1

while x < len(l2) and ret:
    if l2[x] not in l1:
        if off_count == 0:
            ret = False
            break
        off_count -= 1
        x = x +1
    else:
        x = x +1

print("l1: {}".format(l1))
print("l2: {}".format(l2))
print("ret: {}".format(ret))