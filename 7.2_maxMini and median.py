import array as ar


def mean(arra):
    sum = 0
    count = 0
    for i in arra:
        sum += i
        count += 1
    mean = sum / count
    return mean
# Mean == Extra example


def max_min(arra1):
    x = sorted(arra1)
    max1 = x[-1]
    max2 = x[-2]
    min1 = x[0]
    min2 = x[1]
    return max1, max2, min1, min2


def median_f(array):
    sortedLst = sorted(array)
    lenth = len(array)
    index = lenth // 2  # l/2 = 2.5 and l//2 = 2

    if lenth % 2 != 0:
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index - 1]) / 2.0


# arra1 = ar.array('f', [2, 5, 9, 11, 12, 18])   # example for understanding

arra1 = ar.array('f', [25.4, 12.8, 75.7, 5.9, 13.7, 36.8, 87.4, 24.3, 13.8, 11.8, 15.6])
ary1 = [x for x in arra1]

max1, max2, min1, min2 = max_min(ary1)

print(f"""
1st maximum number: {round(max1, 2)}
2nd maximum number: {round(max2, 2)}
1st minimum number: {round(min1, 2)}
2nd minimum number: {round(min2, 2)}\n
median value      : {round(median_f(ary1), 2)}    
""")
