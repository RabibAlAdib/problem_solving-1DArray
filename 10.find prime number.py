import array as ar

def prime(numm):
    p = []
    for num in numm:
        prime = True
        for i in range(2, num):
            if(num%i == 0):
                prime = False

        if prime:
            p.append(num)
        else:
            pass
    return p

print(prime([3,4,5,6,7,8,9]))

inp = input("List: ").split()
lst = [int(x) for x in inp]

arry = ar.array('i',lst)
p = prime(lst)
print("Array: ",arry)
print(f"there are total {len(p)} prime number.")
print("Prime numbers are: ",p)