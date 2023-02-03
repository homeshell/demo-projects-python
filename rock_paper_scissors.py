import random
import os
os.system('cls')

def Play_RockPaperScissors():
    Outcome = 0
    players_move = input("Make your move.. (Rock | Paper | Scissors) -- ").upper()

    if players_move == "EXIT":
        Outcome = 4
        return Outcome

    while (players_move != 'ROCK' and players_move != 'PAPER' and players_move != 'SCISSORS'):
        players_move = input("Type one of the following option: (Rock | Paper | Scissors) -- ").upper()

    computers_move = random.choice(['Rock', 'Paper', 'Scissors']).upper()
    os.system('cls')
    print(f"----- CHOICES -----\nComputer: {computers_move}\nPlayer: {players_move}\n\n| Rock beats Scissors | Scissors beats Paper | Paper beats Rock |\n---- ----- ----- --")

    if players_move == computers_move:
        print("\nRESULT: Stalemate!")
        Outcome = 1
        return Outcome
    
    if DetermineWinner(players_move, computers_move):
        print(f"\nRESULT: Victory!")
        Outcome = 2
        return Outcome
    
    print(f"\nRESULT: Defeat!")
    Outcome = 3
    return Outcome
    
    # r > s, s > p, p > r

def DetermineWinner(YourMove, OpponentMove):
    # return true if player wins

    if (YourMove == 'ROCK' and OpponentMove == 'SCISSORS') or (YourMove == 'SCISSORS' and OpponentMove == 'PAPER') \
        or (YourMove == 'PAPER' and OpponentMove == 'ROCK'):
        return True

print("Welcome to Rock, Paper, Scissors!")

Games_Played = 0
Wins = 0
Ties = 0
Losses = 0
Continue_Playing = True

while Continue_Playing:
    Games_Played += 1
    Game_Outcome = 0

    Game_Outcome = Play_RockPaperScissors()

    if (Game_Outcome == 4):
        Games_Played -= 1
        Continue_Playing = False

    if (Game_Outcome == 2):
        Wins += 1

    elif (Game_Outcome == 1):
        Ties += 1

    elif (Game_Outcome == 3):
        Losses += 1

    print("\n------ ----- ----- STATISTICS BOARD ----- ----- ------")
    print(f"You have played {Games_Played} game.")
    print(f"The game statistics are -- (Wins: {Wins}) (Ties: {Ties}) (Losses: {Losses})")
    if (Losses != 0 or Wins != 0):
        print(f"Win Precentage -- {(Wins/(Wins+Losses)*100)}%")
    print(f"Win Precentage (Including Ties) -- {(Wins/(Wins+Losses+Ties)*100)}%")
    print("TYPE EXIT TO FINISH")
    print("----- ----- ----- ----- ----- ----- ----- ----- ------ ")





