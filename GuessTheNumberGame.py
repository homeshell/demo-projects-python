# Imports useful libraries to add unique functionality to the program.
import random 
import os
# import heartrate
# heartrate.trace(browser=True)

# Cleans terminal for clarity.
os.system('cls')

# Function for calling the main game of the program.
def GuessTheNumber(range, amount_of_tries):
    user_guess = 0
    incorrect_guesses = 0

    # Generates a user random number for the user to guess, based on the range they choose.
    number_to_guess = random.randint(1, range)

    # *** For testing purposes ***
    # print(f"ANSWER -- {number_to_guess}")

    # Masterloop that enables the user to keep guessing as long as they have attempts available and have not correctly guessed.
    while user_guess != number_to_guess:
            # Tells the user how many attempts they have left.
            print(f'Guess remaining -- {amount_of_tries}')
            # Reminds the user of the range to guess between.
            print(f'\nGuess a number between 1 & {range}: ')
            # Runs the integer check function to ensure they enter a proper value.
            user_guess = IntegerChecker_GreaterThanZero()

            # If the user has entered a value that is not within the range determined, prompt them to enter a new value.
            while (user_guess > range or user_guess < 1):
                print(f'Possible numbers are within 1 & {range}: ')
                user_guess = IntegerChecker_GreaterThanZero()

            # Decrements the users tries each time they incorrectly guess.
            amount_of_tries -= 1
            os.system('cls')

            # Code that runs if they correctly guess the randomly generated number.
            if user_guess == number_to_guess:
                incorrect_guesses += 1
                print(f"Well done, that's correct! The answer was: {number_to_guess} ")
                # Ends the function, and returns a true, which later we see adds one to games won.
                if (incorrect_guesses <= 1):
                    print(f"Wow! Only {incorrect_guesses} guess? That's amazing. You had {amount_of_tries} tries left!")
                elif(incorrect_guesses <= 5):
                    print(f"Nice, only {incorrect_guesses} tries? That's not bad. You had {amount_of_tries} tries left!")
                elif(incorrect_guesses > 5):
                    print(f"It took you {incorrect_guesses} tries to crack this code. You did it! You had {amount_of_tries} tries left!")
                return True

            # Helps the user guess the right value
            elif (user_guess < number_to_guess):
                print('HINT: Guess higher!')
                incorrect_guesses += 1
            elif (user_guess> number_to_guess):
                print('HINT: Guess lower!')
                incorrect_guesses += 1

            # Code the executes if the user runs out of tries.
            if amount_of_tries == 0:
                print(f"You're out of attempts! The answer was: {number_to_guess}")
                print(f'Final guess was -- {user_guess}')
                return False
            
            # Reminds the user of their latest guess.
            print(f'Latest guess -- {user_guess}')

# Function for checking if a user input is an integer and is greater than 0.
def IntegerChecker_GreaterThanZero():
    UserInput = input('Enter an integer -- ')

    # Runs until the user enters a valid value. 
    while (True):  
        try: 
            # If the user has not entered an integer, this will not run.
            UserInput = int(UserInput)
            break
        except:
            # Prompts the user to enter an integer value if they accidently entered an incompatible value.
            UserInput = input(f'{UserInput} is not a valid input. (Enter an integer greater than 1) -- ')
    
    # Ensures that the user enters a value greater than 0.
    if (UserInput < 1):
        print(f'{UserInput} is too low, enter 1 or higher.')
        # Function recursion, allows the program to loop through the beginning error handling code to ensure a proper value before comparing its numerical value.
        UserInput = IntegerChecker_GreaterThanZero()
    return int(UserInput)
  
# Function to get either a yes or no answer from the user.
def Get_Yes_or_No():
    # Asks the user if they wish to play again.
    choice_to_continue = input('\nGood going! would you like play again? -- ')

    # Loops until the user enters either yes or no. It is not case sensitive because it is always converted to uppercase, which we account for in our boolean logic.
    while choice_to_continue.upper() != 'YES' and choice_to_continue.upper() != 'NO':
        # Informs the user their value is invalid and what to enter instead.
        choice_to_continue = input(f'{choice_to_continue} is invalid. Enter either yes or no -- ')
    # Returns a value that will terminate the masterloop of the game.
    if choice_to_continue.upper() == 'NO':
        return False 
    # Returns a value that will continue running the program.
    elif choice_to_continue.upper() == "YES":
        print('Another game it is!')
        return True

# Declares important starting values.
continue_game = True
Game_Status_W_or_L = 0
Wins = 0
Loses = 0
Games_Played = 0

# Welcomes the user to the game.
print('Welcome to the number guessing game!')

# Masterloop that enables the program to continue cycling if the user wishes to keep playing.
while (continue_game == True):

    # Keeps track of how many games the user has played.
    Games_Played += 1

    # Gets the range in which the random number will be generated. Example input is 10, range will be from 1 to 10.
    print('\nNumber range?')
    user_selected_range = IntegerChecker_GreaterThanZero()
    os.system('cls')

    # Allows the user to decide how many tries they want to have to guess the number.
    print('How many attempts do you want?')
    attempts_to_correctly_guess = IntegerChecker_GreaterThanZero()
    os.system('cls')

    # Calls the game function, passing in the two parameters just inputted.
    Game_Status_W_or_L = GuessTheNumber(user_selected_range, attempts_to_correctly_guess)

    # Keeps track of their win/loss statistics.
    if (Game_Status_W_or_L == True):
        Wins += 1
    elif (Game_Status_W_or_L == False):
        Loses += 1

    # Displays all relevant game stats for them to see after each game.
    print(f'\nNumber of games played -- {Games_Played}')
    print(f'Current statistics -- (Wins: {Wins})  (Loses: {Loses})')
    print(f'Win precentage -- {(Wins/(Wins + Loses))*100}% ')
    
    # Calls a function that checks if a users input is yes or no.
    Choice_To_Keep_Playing = Get_Yes_or_No()
    # If the user enters no, the masterloop is terminated, ending the program.
    if (Choice_To_Keep_Playing == False):
        print('Thanks for playing, Daisy!')
        continue_game = False

