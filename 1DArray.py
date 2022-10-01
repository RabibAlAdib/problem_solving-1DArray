
# 1 Arrays Forward and Backward
# import array
# inp = input("List: ").split()
# lst = [int(x) for x in inp]
#
# arry = array.array('i', lst)
# print(f"Forwards: {arry}")
# arry.reverse()
# print(f"Backwards: {arry}")



'''-------------------------------'''

# 2 Large Smallest and Average of array
# import array as ar
# import random
#
#
# def Rand(start, end, num):
#     res = []
#     for j in range(num):
#         res.append(random.randint(start, end))
#     return res
#
#
#
# def sum_0f_array(arry):
#     sum = 0
#     for i in arry:
#         sum += i
#     return sum
#
# def check(arry):
#     large = max(arry)
#     smallest = min(arry)
#     sum = sum_0f_array(arry)
#     print(f"Largest Number : {large}")
#     print(f"Smallest Number : {smallest}")
#     print(f"Average Value : {sum}")
#     return ''
#
#
# num = 100
# start = 1
# end = 1000
#
# print(f"Arrays with {num} Random numbers: ")
# arry = ar.array('i', Rand(start, end, num, ))
# print(arry)
# print(check(arry))


# 3
# import array as ar
# import random
#
#
# def Rand_num(start, end):
#     res = []
#     for j in range(25):
#         res.append(random.randint(start, end))
#     return res
#
#
# def Rand_cha(start,end):
#     res = []
#     for j in range(25):
#         res.append(chr(random.randint(ord('a'), ord('z'))))
#         res.append(' ')
#     return res
#
#
# start, end = input("Enter Start and End number: ").split()
# start, end = int(start),int(end)
#
# print(f"Arrays with Random numbers from {start}-{end}: ")
# arry = ar.array('i', Rand_num(start, end))
# print(arry)
#
# F_letter, L_letter = input("Enter Start and End number: ").split()
# print(f"Arrays with Random numbers from {F_letter}-{L_letter}: ")
# arry = ar.array('u', Rand_cha(F_letter, L_letter))
# print(arry)


# 4 find index,

# import random
#
# def Rand_num(size):
#     res = []
#     for j in range(size):
#         res.append(random.choice([x for x in range(1,1000)]))
#     return res
#
#
# num = int(input("Enter the size array: "))
# ran = Rand_num(num)
# arry = ('i', ran)
# print('Array: ', arry)
#
#
# while True:
#     ary = [x for x in arry[1]]
#
#     check = int(input("Check any number from array: "))
#
#     if check in ary:
#         ary_index = arry[1].index(check)
#         ary_count = arry[1].count(check)
#         print(f"{check} was found in in index: ",ary_index)
#         print(f"{check} is found for {ary_count} times")
#     else:
#         print('NUmber not found')
#
