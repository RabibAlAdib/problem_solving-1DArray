# 1 Arrays Forward and Backward
import array

inp = input("List: ").split()
lst = [int(x) for x in inp]

arry = array.array('i', lst)
print(f"Forwards: {arry}")

arry.reverse()
print(f"Backwards: {arry}")