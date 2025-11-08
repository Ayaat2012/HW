# Writing a program to find all the possible sub strings of a string

def sub_string(input_string):
    substrings = []
    n = len(input_string)

    #Iterating through all possible starting indices
    for i in range(n):
        #Iterating through all possible ending indices from current start to end of string
        for j in range(i+1, n+1):
            substrings.append(input_string[i:j])
    return substrings

#Getting user input
input_string = input("Enter your desired string :")
#Result and calling the function
print("The substrings are ", sub_string(input_string))