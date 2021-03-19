#! /usr/bin/env python

in_string = "Mr John smith "

in_array = list(in_string)
out_array = []

for c in in_array:
    if c == " ":
        out_array.append("%20")
    else:
        out_array.append(c)

print("Outarray:" )
print(out_array)

print("out_string")
print("".join(out_array))