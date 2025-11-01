#Check if number is power of 8

def powerOf8(num):

    # Check if number is positive and is power of 2
    if num <= 0 or (num & (num - 1)) == 0:
        return False
    
    
    count = 0
    while num > 1:
        num >>= 1
        count += 1

    # Check if the only set bit is in an even position
    return count % 3 == 0

number = int(input("Enter your number"))
if (powerOf8(number)):
    print(number, "is a power of 8.")
else:
    print(number, "is not a power of 8.")