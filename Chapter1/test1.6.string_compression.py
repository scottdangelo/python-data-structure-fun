#! /usr/bin/env python

in_string = "aabbcddddeeeeffg"
out_string =[]
iter_list = list(in_string)
identical_count = 0

for x, c in enumerate(iter_list):
    count = 0
    if x<(len(in_string)-1) and c == iter_list[x+1]:
        identical_count += 1
    else:
        out_string.append(c)
        if identical_count != 0:
            out_string.append(str(identical_count))
        identical_count = 0

out = ""
print(out_string)
print(out.join(out_string))