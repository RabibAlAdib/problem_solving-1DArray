import array as ar


def fibonacci(num):
    temp = 0
    x = 1
    lst = []
    for i in range(num + 1):
        y = temp + x  # stp 1
        lst.append(temp)
        x = temp
        temp = y
        # print(temp, end=' ')
    return lst


size = int(input("Array Size: "))

num = fibonacci(size)
x = [x for x in num]

arra = ar.array('i', x)

print(arra)
