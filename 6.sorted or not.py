import array as ar


def sorting_chk(array):

    check = sorted(array)
    decending = sorted(array, reverse=True)

    if check == array:
        print("sorted Ascending!")
    elif decending == array:
        print("Sorted Descending!")
    else:
        print("It is not sorted")


inp = input("Enter Array: \n").split()

ary = [int(i) for i in inp]

array = ar.array('i', ary)

sorting_chk(ary)
