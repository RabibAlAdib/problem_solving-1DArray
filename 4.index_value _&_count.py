# 4 find index and count

import random


def Rand_num(size):
    res = []
    for j in range(size):
        res.append(random.choice([x for x in range(1, 1000)]))
    return res


num = int(input("Enter the size array: "))
ran = Rand_num(num)
arry = ('i', ran)
print('Array: ', arry)

while True:
    ary = [x for x in arry[1]]

    check = int(input("Check any number from array: "))

    if check in ary:
        ary_index = arry[1].index(check)
        ary_count = arry[1].count(check)
        print(f"{check} was found in in index: ", ary_index)
        print(f"{check} is found for {ary_count} times")
    else:
        print('NUmber not found')


