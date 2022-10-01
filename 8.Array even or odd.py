import random
import array as ar


def randomN(size):
    lst = []
    for i in range(size):
        lst.append(random.choice([x for x in range(100)]))
    return lst


size = int(input("Array size: "))

x = randomN(size)
lst = [x for x in x]
arra = ar.array('i', x)

odd = []
even = []
for i in lst:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
evenArray = ar.array('i', even)
oddArray = ar.array('i', odd)

print(f"""
Random Array: {arra}
Even Array: {evenArray}
Odd Array: {oddArray}
""")