import random

choices = ["rock", "paper", "scissors", "lizard,", "spock"]

player_score = 0
computer_score = 0

def lost():
    print("You lost!")
    computer_score += 1

def draw():
    print("It´s a draw")
    
def win():
    print("You Won!")
    player_score += 1

def start():
    while True:
        start = input("Do you want to play a game? (y/n) ").lower()
            if start == "y":
                game()
            elif start == "n":
                break
            else:
                print("Please select a correct option")
                   
def game():
    while True:
        player = input("Select your choice - Rock, Paper, Scissors, Lizard, Spock ")
        computer = random(choices)
        print(f"You selected {player} and the computer chose {computer}")
            if player == computer:
                draw()
            elif 