# 2 Large Smallest and Average of array

import array as ar
import random


def Rand(start, end, num):
    res = []
    for j in range(num):
        res.append(random.randint(start, end))
    return res


def sum_0f_array(arry):
    sum = 0
    for i in arry:
        sum += i
    return sum


def check(arry):
    large = max(arry)
    smallest = min(arry)
    sum = sum_0f_array(arry)
    size = len(arry)

    print(f"Largest Number : {large}")
    print(f"Smallest Number : {smallest}")
    print(f"Average Value : {round(float(sum/size),2)}")
    return ''


if __name__ == '__main__':
    num = 100
    start = 1
    end = 1000

    print(f"Arrays with {num} Random numbers: ")
    arry = ar.array('i', Rand(start, end, num, ))
    print(arry)
    print(check(arry))