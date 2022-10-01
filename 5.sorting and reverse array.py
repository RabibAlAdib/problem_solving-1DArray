import array as ar
import random


def randomNum(array1, array2):
    for i, j in (len(array1), len(array2)):
        print()


def Rand_num(size):
    res = []
    for j in range(size):
        res.append(random.choice([x for x in range(1, 100)]))
    return res


def sorting(array1, array2):
    aray1 = sorted(array1, reverse=True)
    aray2 = sorted(array2)
    return aray1, aray2


size = int(input("Size of random numbers: "))

inp1 = Rand_num(size)
inp2 = Rand_num(size)

ary1 = [int(x) for x in inp1]
ary2 = [int(x) for x in inp2]

array1 = ar.array('f', ary1)
array2 = ar.array('f', ary2)

print(f'Array 1 (Before): {array1}')
print(f'Array 2 (Before): {array2}')

aray1, aray2 = sorting(array1, array2)

print(f'Sorting.. \nArray 1 (After): {aray1}')
print(f'Array 2 (After): {aray2}')
