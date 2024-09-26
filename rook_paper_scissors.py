import random

ROCK = 1
PAPER = 2
SCISSORS = 3

PLAYER_WINS = "Player wins!! Woop woop!"
COMPUTER_WINS = "Robocop wins :-("
TIE = "It's a tie!"

def rock_paper_scissors(player_choice):
    computer_choice = random.choice([ROCK, PAPER, SCISSORS])
    choices = {ROCK: "Rock", PAPER: "Paper", SCISSORS: "Scissors"}
    
    print(f"Player chose: {choices[player_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    
    if player_choice == computer_choice:
        print(TIE)
        return TIE
    elif (player_choice == ROCK and computer_choice == SCISSORS) or \
         (player_choice == PAPER and computer_choice == ROCK) or \
         (player_choice == SCISSORS and computer_choice == PAPER):
        print(PLAYER_WINS)
        return PLAYER_WINS
    else:
        print(COMPUTER_WINS)
        return COMPUTER_WINS
x = int(input("choise num between 1 to 3"))        
rock_paper_scissors(x)        