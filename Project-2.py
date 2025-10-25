#Program to check the rightmost set bit in a number
def rightmostSetBit(n):
    count = 1
    while True:
        if (n & 1 == 1):
            break
        else:
            count += 1
        n = n >> 1
        print(count)
n = int(input("Enter your number "))
rightmostSetBit(n)