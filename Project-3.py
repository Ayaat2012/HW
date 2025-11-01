def reverse_bits(n):

    reversed_num = 0

    num_bits = 4

    for i in range(num_bits):
        setbit = (n >> i) & 1
        reversed_num |= (setbit << (num_bits - 1 - i))
    return reversed_num

# Get input from the user
try:
    number = int(input("Enter an integer: "))
    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        reversed_number = reverse_bits(number)
        print(f"Original number: {number} (Binary: {bin(number)})")
        print(f"Reversed bits: {reversed_number} (Binary: {bin(reversed_number)})")
except ValueError:
    print("Invalid input. Please enter an integer.")