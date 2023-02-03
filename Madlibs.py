#  Creating a Madlibs python program using String concatenation. (Putting Strings together)

# Masterloop value, starting off as true.
create_another = True

print("Welcome to my Madlib game! Hope you enjoy.")

while (create_another == True) :

    #  Recieves user input by asking them for a specific piece of the mad lib.
    print("Here we go, time to create something special!")
    adjective = input("Adjective: ")
    verb = input("Verb: ")
    verb2 = input("Verb2: ")
    life_goal = input("Goal in life: ")

    #  Creates the madlib by inserting the variable name in the appropiate spot.
    madlib_display = f"\nMy life is {adjective}, that I love to {verb}. Sometimes though, I just like to {verb2} while contemplating life. Overall, my goal in life is {life_goal}."

    print(madlib_display)

    choice_to_continue = input("\nWow, how great! would you like go again? ")

    #  Error handling
    while choice_to_continue.upper() != 'YES' and choice_to_continue.upper() != 'NO':
        print(choice_to_continue)
        choice_to_continue = input("Try entering yes or no!")

    # Terminates program
    if choice_to_continue.upper() == 'NO':
        create_another = False
        print("It was fun! See ya.")
        



