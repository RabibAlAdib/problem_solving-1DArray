import array as ar


def cont(num, arra):
    return arra.count(num)


# lst = [10, 5, 7, 5, 8, 9, 4, 7, 10]

size = input("Array input: ").split()
lst = [int(x) for x in size]
arra = ar.array('i', lst)

digit = []
for i in lst:
    if i in digit:
        pass
    else:
        digit.append(i)
        print(f"{i} number appear {cont(i, lst)}")