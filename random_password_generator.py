import os
import random
os.system('cls')

# Lists that contain a sufficient amount of characters to create a secure password.
letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols_list = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Get how many of each unique random characters the user wants.
print("Welcome to Homeshell's password generator.")
amount_ran_letters= int(input("Enter amount of letters -- ")) 
amount_ran_symbols = int(input("Enter amount of symbols -- "))
amount_ran_numbers = int(input("Enter amount of numbers -- "))


# Based on amount of letters, symbols or numbers wanted, random.choice() selects
# a random character from the corresponding list, then appends it to a string.

# Random letters selection
random_letters = ""
for pick_letter in range(amount_ran_letters):
    random_letter = random.choice(letters_list)
    # Appends randomly selected character onto a string; random_letters equals each appended random_letter generated.
    random_letters += random_letter

# Random symbols selection
random_symbols = ""
for pick_symbol in range(amount_ran_symbols):
    random_symbol = random.choice(symbols_list)
    # Appends randomly selected character onto a string; random_symbols equals each appended random_symbol generated.
    random_symbols += random_symbol

# Random numbers selection
random_numbers = ""
for pick_number in range(amount_ran_numbers):
    random_number = random.choice(numbers_list)
    # Appends randomly selected character onto a string; random_numbers equals each appended random_number generated.
    random_numbers += random_number

# Creates a password by concatenating a basic string from each randomly generated string, 
# then shuffles the characters of the concatened string.
password = (random_letters + random_symbols + random_numbers)
password_to_list = list(password)
random.shuffle(password_to_list)
randomized_password = ''.join(password_to_list)
print(f"Randomly generated password -- {randomized_password}")


