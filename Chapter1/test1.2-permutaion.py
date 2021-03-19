#! /usr/bin/env python

from setuptools.command.easy_install import main

in_string1 = "qwertym"
in_string2 = "weqrty"

in_array1 = list(in_string1)
in_array2 = list(in_string2)
ret = True

def main():
    if len(in_array1) != len(in_array2):
        return False

    for c in in_array1:
        if c not in in_array2:
            return False
        else:
            in_array2.remove(c)
    return True

print(in_array1)
print(in_array2)

print(main())

if __name__ == "__main__":
    main()