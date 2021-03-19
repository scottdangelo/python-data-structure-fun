#! /usr/bin/env python

in_string1 = "dnvindkjnkfkdj"
in_string = "asdfghjkl"
store = []
ret_val = True

for c in in_string:
    if c in store:
        ret_val =  False
    else:
        store.append(c)

print("Is unique? {}".format(ret_val))

