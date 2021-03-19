#! /usr/bin/env python

in_string = "rad1dar"

leng = len(in_string)-1

my_list = list(in_string.replace(" ","").lower())

ret = True
for i,c in enumerate(my_list):
    print("c: {}, my_list[i]: {},\
           my_list[leng - i]: {}".format(c, my_list[i],
           my_list[leng - i]))
    if my_list[i] != my_list[leng -i]:
        ret = False

print(ret)