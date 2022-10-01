# 3

import array as ar
import random


def Rand_num(start, end):
    res = []
    for j in range(25):
        res.append(random.randint(start, end))
    return res


def Rand_cha(start, end):
    res = []
    for j in range(25):
        res.append(chr(random.randint(ord('a'), ord('z'))))
        res.append(' ')
    return res


# for integer value
start, end = input("Enter Start and End number: ").split()
start, end = int(start), int(end)

print(f"Arrays with Random numbers from {start}-{end}: ")
arry = ar.array('i', Rand_num(start, end))
print(arry)

# for string value
# F_letter, L_letter = input("Enter Start and End number: ").split()
# print(f"Arrays with Random Alphabet from {F_letter}-{L_letter}: ")
# arry = ar.array('u', Rand_cha(F_letter, L_letter))
# print(arry)
