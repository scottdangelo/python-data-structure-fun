#! /usr/bin/env python

input1 = "radarp"
clean = list(input1.replace(" ","").lower())
my_dict = {}
odd_count = 0
for c in clean:
    if c not in my_dict:
        my_dict[c] = 1
    else:
        my_dict[c] += 1

print(my_dict)

for c in my_dict:
    if my_dict[c] %2:
        odd_count = odd_count + 1
if len(input1.replace(" ","")) % 2 == 0: #even
    if odd_count %2:
        print("Not a Palindrome")
    else:
        print("Is a Palindrome")
else: # odd number
    if odd_count > 1:
        print("Not a Palindrome")
    else:
        print("is a palindrome")

    
print(my_dict)


