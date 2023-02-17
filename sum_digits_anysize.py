import os
os.system('cls')

# Get user input, as a string
num_to_sum = input("Enter any sized number to sum: ")
sum_num = 0

# Iterate through the string, num_to_sum, for however long it is. Ex. 7421: Will iterate four times.
for iterations in range(len(num_to_sum)):

    # Creates a new variable and assigns it's value to the current index of the string.
    new_num = num_to_sum[iterations]

    # Creates a new variable which stores the sum of each individual digit. Converts the string into an integer to perform a calculation.
    sum_num = int(num_to_sum[iterations]) + sum_num

# Prints sum of each individual digit. Ex. 5555: Prints 20.
print(sum_num)