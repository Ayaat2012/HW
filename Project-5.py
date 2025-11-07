#Writing a program to find the longest consecutive 1's in the binary representation of a number

def l_c_o(n):

    max_count = 0
    current_count = 0

    while n > 0:
        # checking if the least significant bit is 1 or not
        if (n & 1) == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
        
        # right shift the number to check the next bit
        n >>= 1
    return max_count

n = int(input("Enter your desired number"))
print(f"The longest consecutive 1's in binary of {n} is {l_c_o(n)}")