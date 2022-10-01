def Digit_TO_Binary(num):
    if num >= 1:
        Digit_TO_Binary(num // 2)
    print(num % 2, end='')
    return


# Builtin Function to convert Decimal number to Binary number
def dec_to_bin(num):
    return bin(num).replace("0b", "")


# binary to decimal
def binary_Decimal(n):
    num = n
    dec_value = 0
    base = 1
    temp = num
    while temp:
        last_digits = temp % 10
        temp = int(temp / 10)

        dec_value += last_digits * base
        base = base * 2
    return dec_value


# num = int(input("Convert decimal number to binary: "))

# Digit_TO_Binary(num)       # problem solution
#
# print()
#
# print(dec_to_bin(num))      # Extra
#
# print()
#
# print('{0:b}'.format(num))  # Extra
#
# print()

num = int(input("Convert Binary number to Decimal: "))
print(binary_Decimal(num))

